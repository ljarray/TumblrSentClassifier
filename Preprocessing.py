import sys 
import os
import re

# ---------------------- #
#        FUNCTIONS
# ---------------------- #

def preprocessBank(p):
    if os.path.isdir(p):
        for pp in os.listdir(p):
            if not pp.startswith('.'):
                preprocessBank(p + '/' + pp)
    else:
        f = open(p, 'r')
        text = f.read()

        text = re.sub(r"#", " ", text)
        text = re.sub(r"wa nt", "want", text)

#        text = depunctuate(text)
#        text = killNotes(text)

        f = open(p, 'w')
        f.seek(0) # rewind
        f.write(text)
        f.close()

def depunctuate(t):
    punct = re.compile(r"[^#\w\s]") # grabs punctuation minus hashtags
    text_list = punct.split(t)
    new_t = ''
    for i in range(len(text_list)):
        new_t = new_t + text_list[i]
    return new_t  

def killNotes(t):
    notes = re.compile(r"(\d+\snotes)|(\d\snote)")
    if len(notes.split(t)) > 0:
        return notes.split(t)[0]
    else:
        return t

# ---------------------- #
#       RUN LOGIC
# ---------------------- #

preprocessBank('corpus/preprocessed')