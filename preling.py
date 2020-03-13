import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# commented lines not required if resources are already downloaded
# nltk.download("wordnet")
# nltk.download("punkt")

# nltk_to_wordnet_pos - helper function to get the wordnet equivalent
# of an NLTK part-of-speech symbol.
def nltk_to_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswitch('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def sentence_data(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_list = nltk.pos_tag(tokens)
    lemma_list = [lemmatizer.lemmatize(elem[0], nltk_to_wordnet_pos(elem[1])) for elem in pos_list]
    return 0
    #return [{"pos" : pos_list[i], "lemma" : lemma_list[i]} for i in range(0, len(pos_list)}]

print(sentence_data("The cat sat on the mat."))
