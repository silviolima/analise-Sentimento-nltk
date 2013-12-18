# -*- coding: utf-8 -*-
import re
import sys

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

if __name__ == '__main__':

    if ( len(sys.argv) == 2):  
        print ('\n') 
        #Read the tweets one by one and process it
        arq = sys.argv[1]
        fp = open(arq, 'r')
        print("\n")
        i=1
        line = fp.readline()
        while (line):
            processedTweet = processTweet(line)
            if (line): print ("Mensagem %d - \n\t%s \n" %(i,processedTweet))
            line=fp.readline()
            i=i+1
        fp.close()
    else:
        print ('\nUsage: python preProcess1.py file\n') 


    
