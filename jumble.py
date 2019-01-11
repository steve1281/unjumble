#!/usr/bin/env python

import os
import sys
import itertools
import mmap

# assume list of words in same directory as script. (adjust if not the case)
# Note: Currently using dictionary from github dwyl/english-words
DICT_PATH = os.path.dirname(os.path.abspath(__file__)) + '/words_alpha.txt'

def scan_words(s, n):
    """ produce a list of unique perms and print the ones in the dictionary """
    t = list(set(itertools.permutations(s, n)))
    for i in range(len(t)):
        if check_word("".join(t[i])):
            print ("".join(t[i]))

def check_word(word):
    """ scan dictionary for matches. Note this is a HUGE file; use mmap """
    found = False
    with open(DICT_PATH, 'rb') as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Note that each word terminates with \r\n.
        if s.find('\n'+word+'\r') != -1:
            return True

def main():
    """ main - figure out the source for the jumble and scan """
    if len(sys.argv) ==1:
        s = 'abc'
    else:
        s = sys.argv[1]

    if len(sys.argv) ==2:
        n = len(s)
    else:
        print ('This might take a while')
        n =  int(sys.argv[2])

    print ('Jumble is: %s %d' % (s, n))
    scan_words(s, n)
    

if __name__ == '__main__':
    main()
