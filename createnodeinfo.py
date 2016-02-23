from readsentence import *
import nltk
stopwords = nltk.corpus.stopwords.words('english')

def nodeinfo(i):
    anns = readanns(i)
    sentence = [t['caption'] for t in anns]
    sen_list = [nltk.word_tokenize(t) for t in sentence]
    sen_list_word=[]
    for v in sen_list:
        sen_list_word.append([ w for w in v if w != ',']) 
    return sen_list_word