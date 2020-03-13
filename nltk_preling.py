# preling.py - NLTK pre-linguistic analysis functions for PySemRep.
# Written by Srihari Nanniyur.

import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# next few lines not required if resources are already downloaded
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# nltk_to_wordnet_pos() - helper function to convert POS tags.
# Takes an NLTK POS tag string as input and returns its WordNet POS equivalent.
def nltk_to_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN # default type for wordnet is noun anyway

# sentence_data() - work in progress.
# Currently returns POS and lemma on a per-word basis in a sentence.
# Still need to implement chunking.
def sentence_data(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_list = nltk.pos_tag(tokens)
    lemma_list = [lemmatizer.lemmatize(elem[0], nltk_to_wordnet_pos(elem[1])) for elem in pos_list]
    return [{"word":pos_list[i][0], "pos":pos_list[i][1], "lemma":lemma_list[i]}
        for i in range(0, len(pos_list))]

print(sentence_data(open("test.plain", "r").read()))
