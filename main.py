# main function

import web
from web import form
import hashlib
import sys
sys.path.append('./code')
import re
import GetStateList
import TwitterStream
import Display
import GetLatiLongi


urls = (
    r'/', 'index',
    r'/index', 'index',
    r'/(.*\.js)', 'javascript',
    r'/login', 'login',
    r'/register', 'register'
)
app = web.application(urls, globals())


render = web.template.render('templates/')


class index:
    def GET(self): # get method
        form = text()
        return render.formtest(form)

    def POST(self): # post method
        postdata = web.data()
        postdata = postdata.split("&")
        webinput=dict()
        for pair in postdata:
            pair=pair.split("=")
            webinput[pair[0]]=pair[1]
        keywords = webinput['Keywords'].encode("utf-8")
        language = webinput['Language'].encode("utf-8")
        location = webinput['Location']
        if 'Time' in webinput.keys():
            time = webinput['Time']
        else:
            time = (webinput['day'], webinput['hour'], 
                    webinput['minute'],webinput['second'])
            print time

        keywords = keywords.split(' ')
        languages = list()
        languages.append(language)
        LatiLongi = GetLatiLongi.GetLatiLongi()[location]

        return Display.Display(TwitterStream.TwitterStream(kwords=keywords,
                                                           lang=languages,
                                                           lim=time,
                                                           loca=LatiLongi))


class login:
    def POST(self):
        postdata = web.data()
        postdata = postdata.split("&")
        webinput=dict()
        for pair in postdata:
            pair=pair.split("=")
            webinput[pair[0]]=pair[1]
        username = webinput['username'].encode("utf-8")
        passwd = webinput['password'].encode("utf-8")
        f = open('./data/userinfo', 'r')
        userinfo = dict()
        for line in f:
            nline = line.strip().split('\t')
            userinfo[nline[0]] = nline[1]
        if username not in userinfo:
            return 'User name does not exist'
        else:
            if userinfo[username] != hashlib.md5(passwd).hexdigest():
                return 'Wrong password'
            else:
                form = text()
                return render.formtest2(form, username.replace('%40', '@'))


class register:
    def POST(self):
        postdata = web.data()
        postdata = postdata.split("&")
        webinput=dict()
        for pair in postdata:
            pair=pair.split("=")
            webinput[pair[0]]=pair[1]
        username = webinput['username']
        passwd = webinput['password'].encode("utf-8")
        passwda = webinput['passwordagain'].encode("utf-8")
        if passwd != passwda:
            return 'Invalid Password!'
        print username
        print re.match('[^@]+@[^@]+\.[^@]+', username)
        if re.match('[^@]+%40[^@]+\.[^@]+', username) == None:
            return 'Please use email as username'
        else:
            out = open('./data/userinfo', 'aw')
            out.write('%s\t%s\n' % (username, hashlib.md5(passwd).hexdigest()))
            return 'Successful, %s' % username.replace('%40', '@')


class javascript:
    def GET(self, file):
        try:
            f = open(file, 'r')
            return f.read()
        except:
            return file + " 404 Not Found"

			
text = form.Form(
    form.Textarea('Keywords', rows=1, cols=50, value=''),
    form.Dropdown('Language', [('en', 'English')]),
    form.Dropdown('Time', [('5', 'Lastest 5'), ('10', 'Lastest 10')]),
    form.Dropdown('Location', [('us', 'United States'), ('ww', 'Worldwise')]),
)


if __name__ == "__main__": 
    app.run()
