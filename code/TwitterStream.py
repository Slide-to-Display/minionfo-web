from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os


consumer_key = "xE6YyJ7KDH3f3JhJb8TkMA"
consumer_secret = "46HY9vzudfOja3Ret3OJdebnpjA7A57eV1Out45ec"
access_token = "1965403830-gQQZP80il05uQ7DtYY4AVhaXZDj3nEa60nZ9nWE"
access_token_secret = "QSWxzGjDXkGV1KwMSWdGZEvntqoEfGTureqfnUZOm8"


class StdOutListener(StreamListener):
    def on_data(self, data):
        # out.write('%s\n' % data)
        results.append(data)
        if len(results) < limit:
            return True
        else:
            return False

    def on_error(self, status):
        print status


def TwitterStream(kwords, lang=['en'], lim=1, loca=[-180,-90,180,90]):
    # print kwords, lang, lim, loca
    # try: os.makedirs(os.getcwd() + '/output')
    # except: pass
    # global out
    # out = open(os.getcwd() + '/output/' + '-'.join(keywords), 'w')
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    global results
    results = list()
    global limit
    limit = lim
    stream = Stream(auth, l)

    stream.filter(track=kwords, languages=lang)
    # stream.filter(track=kwords)
    # def filter(self, follow=None, track=None, async=False, locations=None,
    #            stall_warnings=False, languages=None, encoding='utf8'):
    return results


if __name__ == '__main__':
    import json
    # for i in TwitterStream(['iphone']):
    #     d = json.loads(i)
    #     print d['text']
        # print d['lang']
        # print d['place']
        # print ''
