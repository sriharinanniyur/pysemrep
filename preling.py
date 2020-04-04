# preling.py - NLTK pre-linguistic analysis functions for PySemRep.
# Written by Srihari Nanniyur.

import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
import pprint
import chunk

pp = pprint.PrettyPrinter(indent=4)

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
def sentence_data(text):
    tokens = nltk.word_tokenize(text)
    pos_list = nltk.pos_tag(tokens)
    lemma_list = [lemmatizer.lemmatize(elem[0], nltk_to_wordnet_pos(elem[1])) for elem in pos_list]
    fmt_text = ""
    for i in range(0, len(tokens)):
        fmt_text += str(tokens[i]) + "_" + str(pos_list[i][1]) + " "
    chunks = str(chunk.chunker.parse(fmt_text))
    #chunks = " ".join([word.split("_")[0] for word in chunks.split()])
    return str(chunks)

for sentence in sent_tokenize(open("test.plain", "r").read()):
    print(sentence_data(sentence))
