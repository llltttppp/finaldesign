from readsentence import *
import nltk
stopwords = nltk.corpus.stopwords.words('english')

def nodeinfo(i):
    anns = readanns(i)
    sentence = [t['caption'] for t in anns]
    sen_list = [nltk.word_tokenize(t) for t in sentence]
    sen_list_word=[]
    for v in sen_list:
        sen_list_word.append([ w.lower() for w in v if (w != ',' and w != '.' and w != '!')]) 
    sen_list_word = [nltk.pos_tag(v) for v in sen_list_word]
    for k in sen_list_word:
        for t in range(0,len(k)):
            if(k[t][0] in stopwords):k[t]=(k[t][0],'STD')
    return sen_list_word

