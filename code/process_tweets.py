# sentiment analysis function
import re
import os
import json
import subprocess
from Tweet import Tweet



# problem I see with Stanford coreNLP is that, it doesnt preprocess tweets
# so for tweet like "the new iPhone is #ugly" outputs positive since it only detects new, which is positive, and is not able to detect #ugly
# negativity of "the new iPhone is ugly" will be detected
def process_raw_tweet(tweet):
	# Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to ''
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    # Convert @username to ''
    tweet = re.sub('@[^\s]+','',tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Replace #word with word
    # Need more detail sub, #SoUgly => so ugly
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # Replace punctuation
    tweet = re.sub('[!?.]', ',', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet

def extract_fetched_tweets(raw_twitter_input):
	tweets = []
	processed_tweets = ''
	# json_file = open(raw_twitter_input)
	# json_data = json.load(json_file)
	# json_file.close()
        json_data = raw_twitter_input
	for tweet in json_data:
                tweet = json.loads(tweet)
		tweets.append(Tweet(tweet['text'].encode('utf-8'), tweet['user']['location'].encode('utf-8')))
		processed_tweets += process_raw_tweet(tweet['text'].encode('utf-8')) + '\n'
	return tweets, processed_tweets

def analyse_tweets(tweets, processed_tweets):
        print os.path.dirname(os.path.abspath(__file__))
	proc = subprocess.Popen(["java -cp '%s/stanford-corenlp/*' -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -stdin" % os.path.dirname(os.path.abspath(__file__))],
                                stdin = subprocess.PIPE, 
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE, 
                                shell = True)
	stdout_data = proc.communicate(input=processed_tweets)[0].strip().split('\n')
	count = 0
	for sentiment in stdout_data:
            tweets[count].sentiment = sentiment.strip()
            count+=1

def process_analyser_output():
	pass



if __name__ == '__main__':
	tweets, processed_tweets = extract_fetched_tweets("raw_twitter_input.json")
	analyse_tweets(tweets, processed_tweets)

	#print "====="
	#print processed_tweets
	print "====="


	for tweet in tweets:
		print tweet
