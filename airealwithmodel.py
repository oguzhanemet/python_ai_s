import random
import pickle
from collections import defaultdict


with open('ngram5_markov_chain.pkl', 'rb') as f:
    markov_chain = pickle.load(f)

def generate_ngram_paragraph(markov_chain, gender, num_sentences=10, n=4):
    paragraph = []
    for _ in range(num_sentences):
        sentence = None
        while sentence is None:
            
            current_key = random.choice([key for key in markov_chain.keys() if key[0][0].isupper()])
            current_sentence = list(current_key)
            while current_key in markov_chain:
                next_word = random.choice(markov_chain[current_key])
                current_sentence.append(next_word)
                current_key = tuple(current_sentence[-n:])
                if next_word.endswith('.'):
                    break
            
            temp_sentence = ' '.join(current_sentence).strip()
            if not temp_sentence.endswith('.'):
                temp_sentence += '.'
            
            
            if gender == 'male' or ('female' not in temp_sentence):
                sentence = temp_sentence

        paragraph.append(sentence)
    return ' '.join(paragraph)


paragraph = generate_ngram_paragraph(markov_chain, gender='male', num_sentences=10, n=4)
print(paragraph)