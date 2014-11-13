from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import time


consumer_key = "xE6YyJ7KDH3f3JhJb8TkMA"
consumer_secret = "46HY9vzudfOja3Ret3OJdebnpjA7A57eV1Out45ec"
access_token = "1965403830-gQQZP80il05uQ7DtYY4AVhaXZDj3nEa60nZ9nWE"
access_token_secret = "QSWxzGjDXkGV1KwMSWdGZEvntqoEfGTureqfnUZOm8"


class StdOutListener(StreamListener):
    def on_data(self, data):
        results.append(data)
        if len(results) < limit:
            return True
        else:
            return False

    def on_error(self, status):
        print status


class StdOutListener_time(StreamListener):
    def on_data(self, data):
        if 'text' in data:
            results.append(data)
        # print data
        if time.time() < limit:
            return True
        else:
            return False

    def on_error(self, status):
        print status


def TwitterStream(kwords, lang=['en'], lim='1', loca=[-180,-90,180,90]):
    # print kwords, lang, lim, loca
    global limit
    if 's' not in lim and 'h' not in lim:
        l = StdOutListener()
        limit = int(lim)
    else:
        l = StdOutListener_time()
        if lim == '5s':
            limit = time.time() + 5
        else:
            limit = time.time() + 3600 * int(lim.replace('h', ''))

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    global results
    results = list()
    stream = Stream(auth, l)

    stream.filter(track=kwords, languages=lang, locations = loca)
    # def filter(self, follow=None, track=None, async=False, locations=None,
    #            stall_warnings=False, languages=None, encoding='utf8'):
    return results


if __name__ == '__main__':
    import json
    for i in TwitterStream(['iphone'], lim = '5s'):
        print i
        d = json.loads(i)
        print d['text']
        print d['lang']
        print d['place']
        print ''
