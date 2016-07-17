import sys 
import re
import numpy
import nltk
from random import shuffle
from nltk.classify import *
from nltk.tag import tuple2str
from MakeCorpus import *
#   from nltk.collocations import BigramCollocationFinder
#   from nltk.metrics import BigramAssocMeasures

def makeTraining(lemma=False, stop=False, count=False, weight=False):
    print "\n\tMaking the corpus..."
    c = Corpus("corpus/preprocessed", lemma, stop, count, weight);
    
    featuresets = []
    for p in c.post_names:
        if not count and not weight:
            featuresets.append((dict([('%s' %tuple2str(f), 1) for f in c.posts[p].features]), c.posts[p].label))
            # print featuresets
        elif not weight:
            featuresets.append((dict([('%s' %tuple2str(f), c.posts[p].feature_count[f[0]]) for f in c.posts[p].features]), c.posts[p].label))
        else:
            featuresets.append((dict([('%s' %tuple2str(f), c.posts[p].feature_count[f[0]]*c.sentweight[f]) for f in c.posts[p].features]), c.posts[p].label))
    avg = 0
    test_set = []
    train_set = []
    for i in range(5):
        for j in range(250):
            if j % 5 == i:
                test_set.append(featuresets[j])
            else:
                train_set.append(featuresets[j])
        classifier = nltk.classify.maxent.MaxentClassifier.train(train_set, count_cutoff=0, algorithm='GIS',  max_iter=25)
        print "\n\tMost Informative Features\n\t-------------------------------------\n"
        classifier.show_most_informative_features(10)
        avg += nltk.classify.accuracy(classifier, test_set)
    print "\n\tAccuracy on Test Data           %s\n\t-------------------------------------\n" %"{:.3f}".format(avg/5)
    print "\n\n"


def runExp():
    e = { '1' : [False, False, False, False], '2' : [True, False, False, False], '3' :[False, True, False, False], '4' : [False, False, True, False]}
    valid = ["1", "2", "3", "4"]

    print """\tExperiments:
    \t-------------------------------------
    \t1) Bag of Words
    \t2) Bag of Words (with Lemmatization)
    \t3) Bag of Words (with Stopwords removed)
    \t4) Bag of Words (with Word Counts)"""
    
    exp = str(raw_input("\n\tWhich would you like to run?\n\t")).strip()

    breaker = 0
    while exp not in valid and breaker < 5:
        exp = str(raw_input("\n\tThat's not an experiment. Which experiment would you like to run?\n\t")).strip()
        breaker += 1

    makeTraining(e[exp][0],e[exp][1],e[exp][2],e[exp][3])

    cont = str(raw_input("\tWould you like to run another experiment? (Y/N)\n\t")).lower().strip()

    if cont == "y":
        runExp()
    else:
        print "\n\tOkay, goodbye.\n\n"

# -------------------------------------- #
#               TEST CODE
# -------------------------------------- #

print "\n\n\n\n"
print """\t   ______                __    __        ________                _ _____
\t  /_  __/_  ______ ___  / /_  / /____   / ____/ /___ ___________(_) __(_)__  _____
\t   / / / / / / __ `__ \/ __ \/ / ___/  / /   / / __ `/ ___/ ___/ / /_/ / _ \/ ___/
\t  / / / /_/ / / / / / / /_/ / / /     / /___/ / /_/ (__  |__  ) / __/ /  __/ /    
\t /_/  \__,_/_/ /_/ /_/_.___/_/_/      \____/_/\__,_/____/____/_/_/ /_/\___/_/     \n\n"""

runExp()







