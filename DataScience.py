# Use NLTK Downloader to download averaged_perceptron_tagger first
import nltk


#text = input('Enter text: ')

# Tokenisation
from nltk.tokenize import word_tokenize,sent_tokenize

#tokenized = word_tokenize(text)

# Stop Words
import string
from nltk.corpus import stopwords
def stop_words(tokenized):
    punctuation = list(string.punctuation) #['.',',',':',';','?','!']
    stop_words = list(stopwords.words("english"))
    #stop_words = ['a','as','at','they','the','his','her','so','and','were','from',
    #              'that','of','in','only','with','to']
    included_punctuation = [word for word in tokenized 
                            if word.lower() in punctuation]
    included_stop_words = [word for word in tokenized 
                           if word.lower() in stop_words]
    everything_else = [word for word in tokenized 
                       if word.lower() not in set(stop_words + punctuation)]
    return everything_else,included_stop_words,included_punctuation

# Stemming and Lemming
from nltk.stem import PorterStemmer, LancasterStemmer
def stemlem(tokenized):
    stemmer = PorterStemmer()
    lemmatizer = nltk.WordNetLemmatizer()
    return [ [w,stemmer.stem(w),lemmatizer.lemmatize(w)] 
    for w in list(set(tokenized))]
    
# POS Tagging
def pos_tagging(tokenized):
    tagged =  nltk.pos_tag(list(set(tokenized)))
    tagged = [(t[0],t[1]) for t in tagged]
    return tagged

# Bi/Trigrams
from nltk import bigrams, trigrams
def grams(tokenized):
    return list(bigrams(tokenized)), list(trigrams(stop_words(tokenized)[0]))
    
# Frequency related statistics
from collections import Counter
import math
def frequency_statistics(text):
    words = word_tokenize(text)
    # Organisation
    words = list(set(stop_words(words)[0])) +\
    list(set(stop_words(words)[1])) +\
    list(set(stop_words(words)[2]))
    sents = sent_tokenize(text) 
    #filtered = stop_words(words)
    tf= {word:Counter(word_tokenize(text))[word] for word in words} #Term Frequency
    df = {}
    for word in words:
        df[word] = 0
        for sent in sents:
            if word in sent: df[word]+=1
    idf = {word: math.log(len(sent)/df,10) for (word, df) in  df.items()}
    tfidf = {word: tf[word]*idf[word] for word in words}
    #Processing
    stats = []
    for word in words:
        stats += [[word,tf[word],df[word],idf[word],tfidf[word]]]
    return stats

# Update 
if __name__ == '__main__':
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    nltk.download('wordnet')
    #nltk.download('tagsets')
