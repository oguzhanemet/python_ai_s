import pandas as pd
import random
import pickle
from collections import defaultdict


df = pd.read_csv('CS_PATH', encoding='iso-8859-9', on_bad_lines='skip')
sentences = df['row'].dropna().tolist() 


def clean_sentence(sentence):
    return sentence.strip().replace('\n', ' ').replace('\r', ' ')

sentences = [clean_sentence(sentence) for sentence in sentences]

def build_ngram_markov_chain(sentences, n=4):
    markov_chain = defaultdict(list)
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - n):
            key = tuple(words[i:i+n])
            markov_chain[key].append(words[i+n])
    return markov_chain

n = 4  
markov_chain = build_ngram_markov_chain(sentences, n)


with open('ngram5_markov_chain.pkl', 'wb') as f:
    pickle.dump(markov_chain, f)