import nltk
import os
import random
from nltk.tokenize import *
from nltk.classify import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.tag import pos_tag

wnl = WordNetLemmatizer()

class Corpus(object):
    post_names = [] # list of names of the files
    posts = {} # directory of post_names as the keys for each Post object
    words = []
    sent_weight = {}
    feature_list = []
    stops = set(stopwords.words('english'))

    def __init__(self, p, lemma=False, stop=False, count=False, weight=False):
        self.makePostBank(p)
        random.shuffle(self.post_names)
        if lemma:
            self.words = self.dalaiLemma()
        if stop:
            self.words = self.pullAllTheStops() 
        temp_list = Counter(self.words).most_common(1000)
        for word in temp_list:
            self.feature_list.append(word[0])
        # print self.feature_list[:30]

        for p in self.post_names:
            self.posts[p].setFeatures(self.feature_list, lemma)
            if count:
                self.posts[p].setFeatureCount()
            # print self.posts[self.post_names[i]].features
#        for p in self.post_names:
#            self.posts[p].setFeatures(self.feature_list, lemma)

    def makePostBank(self, p):
        if os.path.isdir(p):
            for pp in os.listdir(p):
                if not pp.startswith('.'):
                    self.makePostBank(p + '/' + pp)
        else:
            self.post_names.append(p)
            # print p
            if not p in self.posts:
                self.posts[p] = Post(p)
                # print self.posts[p]
                self.words.extend(nltk.tokenize.word_tokenize(self.posts[p].text))

    def dalaiLemma(self):
        lemmas = []
        for word in self.words:
            lemmas.append(wnl.lemmatize(word))
        return lemmas

    def pullAllTheStops(self):
        stopwords = []
        for word in self.words:
            if word not in self.stops:
                stopwords.append(word)
        return stopwords

    def __str__(self):
        print_list = ''
        for j in range(25):
            i = random.randrange(1000)
            print_list += self.feature_list[i] + '\n'
        return print_list

    def printFirst(self, n):
        for i in range(n):
            print self.post_names[i] + "    |    " + self.posts[self.post_names[i]].label

    def printRandom(self, n):
        for j in range(n):
            i = random.randrange(250)
            print self.post_names[i] + "    |    " + self.posts[self.post_names[i]].label

class Post(object):
    path = '' # the path
    label = '' # the sentiment label, pulled from directory name
    text = '' # the post text
    features = []
    feature_count = {}

    def __init__(self, p):
        self.path = p
        self.label = os.path.basename(os.path.dirname(p))
        # print self.label

        f = open(p, 'r')
        self.text = f.read().lower()
        # print self.text

    def setFeatures(self, feats, lemma=False):
        self.features = pos_tag(nltk.tokenize.word_tokenize(self.text))
        for group in self.features:
            word, tag = group[0], group[1]
            if lemma:
                self.features.remove(group)
                word = wnl.lemmatize(word)
                self.features.append((word,tag))           
            # print group
            if word not in feats:
                if group in self.features:
                    self.features.remove(group)
                    # print "Group removed."
        # print self.features

    def setFeatureCount(self):
        temp_list = Counter(self.features)
        # print temp_list
        for word in temp_list:
            # print word
            self.feature_count[word[0]] = temp_list[word]
            # print self.feature_count[word[0]]
        # print self.feature_count

    def __str__(self):
        return self.label

# ---------------------- #
#       TEST CODE
# ---------------------- #

# corp = makeCorpus('corpus/preprocessed')
# print corp
# corp.printSample(15)

