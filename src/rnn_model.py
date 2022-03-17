import numpy as np
import torch
from tqdm import tqdm
from utils import get_device
import torch.nn.functional as F

DEVICE = get_device()


class LSTMModel(torch.nn.Module):
    def __init__(self, hidden_size=128):
        super().__init__()

        self.model_rnn = torch.nn.LSTM(
            input_size=37, hidden_size=hidden_size, bidirectional=False, batch_first=True)
        self.model_dense = torch.nn.Sequential(
            torch.nn.Linear(  hidden_size, 1),
            # torch.nn.ReLU(),
            # torch.nn.Linear( 128, 1),
            torch.nn.Sigmoid(),
        )

        self.loss = torch.nn.BCELoss()
        self.loss_without_reduce = torch.nn.BCELoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-6)

        self.to(DEVICE)

    def forward(self, x):
        seq_length = x.shape[0]
        # TODO: verify this is correct
        x = x.reshape(1, seq_length, 37)

        # take (1) the output, (2) the first sample and (3) the last item in sequence
        x = self.model_rnn(x)[0][0][-1]

        # projection layer
        x = self.model_dense(x)

        return x

    def eval_dev(self, data_dev):
        self.train(False)
        losses_dev = []
        hits = []
        with torch.no_grad():
            for sample, label in tqdm(data_dev):
                sample = torch.Tensor(sample).to(DEVICE)

                out = self.forward(sample)
                loss = self.loss_without_reduce(out, torch.Tensor([label]))
                if (out > 0.5 and label == 1) or (out <= 0.5 and label == 0):
                    hits.append(1)
                else:
                    hits.append(0)
                losses_dev += loss.detach().cpu().tolist()

        losses_dev = np.average(losses_dev)
        self.train(True)
        return losses_dev, hits

    def train_loop(self, data_train, data_dev, prefix="", epochs=50):
        logdata = []
        for epoch in range(epochs):
            self.train(True)

            losses_train = []
            hits_train = []
            for sample_i, (sample, label) in enumerate(tqdm(data_train)):
                sample = torch.Tensor(sample).to(DEVICE)

                print(f"train acc: {np.average(hits_train):.2%}")
                out = self.forward(sample)
                loss = self.loss(out, torch.Tensor([label]))

                if (out > 0.5 and label == 1) or (out <= 0.5 and label == 0):
                    hits_train.append(1)
                else:
                    hits_train.append(0)

                # backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                losses_train.append(loss.detach().cpu().item())

            losses_train = np.average(losses_train)

            # one dev step
            losses_dev, hits_dev = self.eval_dev(data_dev)

            print(f"dev acc: {np.average(hits_dev):.2%}")

            # warning: train_loss is macroaverage, dev_loss is microaverage
            logdata.append({
                "epoch": epoch,
                "train_loss": losses_train,
                "train_acc": np.average(hits_train),
                "dev_loss": losses_dev,
                "dev_acc": np.average(hits_dev)
            })

            # save_json(
            #     f"computed/{prefix}-f{self.fusion}.json",
            #     logdata
            # )
            losses_train = []
