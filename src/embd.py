
import torch
from transformers import BertTokenizer, BertModel
from transformers import AutoTokenizer, AutoModel
from utils import get_device
from tqdm import tqdm
from argparse import ArgumentParser

DEVICE = get_device()


def mean_pooling(model_output, attention_mask, layer_i=0):
    # Mean Pooling - Take attention mask into account for correct averaging
    # first element of model_output contains all token embeddings
    token_embeddings = model_output[layer_i]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(
        token_embeddings.size()
    ).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return (sum_embeddings / sum_mask).reshape(-1)


class BertWrap():
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(
            "bert-base-cased"
        )
        self.model = BertModel.from_pretrained(
            "bert-base-cased", return_dict=True, output_hidden_states=True
        )
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence, type_out):
        encoded_input = self.tokenizer(
            sentence, padding=True,
            truncation=True, max_length=128,
            return_tensors='pt'
        )
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask'])
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")


class SentenceBertWrap():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model = AutoModel.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence, type_out):
        encoded_input = self.tokenizer(
            sentence, padding=True, truncation=True, max_length=128, return_tensors='pt')
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask']
            )
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")
