import web
from web import form
import sys
sys.path.append('./code')
import GetStateList
import TwitterStream
import Display
import GetLatiLongi


urls = (
    '/', 'index',
)
app = web.application(urls, globals())


render = web.template.render('templates/')


class index:
    def GET(self):
        form = text()
        return render.formtest(form)

    def POST(self):
        webinput = web.input()
        keywords = webinput['Keywords'].encode("utf-8")
        language = webinput['Language'].encode("utf-8")
        time = webinput['Time']
        location = webinput['Location']

        keywords = keywords.split(' ')
        languages = list()
        languages.append(language)
        LatiLongi = GetLatiLongi.GetLatiLongi()[location]
        return Display.Display(TwitterStream.TwitterStream(kwords=keywords,
                                                           lang=languages,
                                                           lim=int(time),
                                                           loca=LatiLongi))
text = form.Form(
    form.Textarea('Keywords', rows=1, cols=50, value=''),
    form.Dropdown('Language', [('en', 'English')]),
    form.Dropdown('Time', [('5', 'Lastest 5'), ('10', 'Lastest 10')]),
    form.Dropdown('Location', [('us', 'United States'), ('ww', 'Worldwise')]),
)


if __name__ == "__main__": 
    app.run()
