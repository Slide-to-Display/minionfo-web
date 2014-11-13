# display function

import json
import process_tweets



def Display(data):
    results = list()

    tweets, processed_tweets = process_tweets.extract_fetched_tweets(data)
    process_tweets.analyse_tweets(tweets, processed_tweets)
    for tweet in tweets:
        results.append('text: %s\nsentiment: %s\n===\n' \
                       % (tweet.tweet, tweet.sentiment))

    # for i in data:
    #     d = json.loads(i)

    #     text = d['text'].encode("utf-8")
    #     lang = d['lang'].encode("utf-8")
    #     created_time = d['created_at'].encode("utf-8")
    #     place = 'None'
    #     if d['place'] != None:
    #         place = d['place']['full_name'].encode("utf-8")

    #     # results.append('%s\n' % text)
    #     results.append('text: %s\nlang: %s\ncreated_time: %s\nplace: %s\n===\n' \
    #                    % (text, lang, created_time, place))

    return '\n\n'.join(results)
    

if __name__ == '__main__':
    pass
