'''
Created on 03-May-2014

@author: rahul
'''
import re


def reverse(sentence):
    '''
        Returns a re    ed sentence.
    '''
    def string_reverse(matchobj):
        '''
            Returns reversed string.
        '''
        string_data = matchobj.group(0)
        return string_data[::-1]

    return re.sub("([a-zA-Z-]+)", string_reverse, sentence)

if __name__ == "__main__":
    sentence = raw_input("Sentence to reverse: ")
    print "Reversed sentence : ", reverse(sentence)
