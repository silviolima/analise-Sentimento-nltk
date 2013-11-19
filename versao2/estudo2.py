import nltk

pos_tweets = [('I love this car', 'positive'),
  		  ('This view is amazing', 'positive'),
			  ('I feel great this morning', 'positive'),
			  ('I am so excited about the concert', 'positive'),
			  ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

tweets = [
    (['love', 'this', 'car'], 'positive'),
    (['this', 'view', 'amazing'], 'positive'),
    (['feel', 'great', 'this', 'morning'], 'positive'),
    (['excited', 'about', 'the', 'concert'], 'positive'),
    (['best', 'friend'], 'positive'),
    (['not', 'like', 'this', 'car'], 'negative'),
    (['this', 'view', 'horrible'], 'negative'),
    (['feel', 'tired', 'this', 'morning'], 'negative'),
    (['not', 'looking', 'forward', 'the', 'concert'], 'negative'),
    (['enemy'], 'negative')]

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]



def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
        print("Document : %s "%document)
    	document_words = set(document)
    	features = {}
    	for word in word_features:
                print "Word: %s  Msg: %s "%(word,document)  
        	features['contains(%s)' % word] = (word in document_words)
    	return features


training_set = nltk.classify.util.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("\n\n\tDepois de gerar claissifer\n\n")

print classifier.show_most_informative_features(32)

tweet = 'Larry is not  my best friend'
print("\n\tFrase: Larry is not my best friend")
print classifier.classify(extract_features(tweet.split()))
#positive

print extract_features(tweet.split())

print classifier.show_most_informative_features(32)

tweet = 'Your song is not great best'
print ("\n\tFrase 2: Your song is not  great best")
print classifier.classify(extract_features(tweet.split()))
print classifier.show_most_informative_features(32)
# positive
