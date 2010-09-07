import os, os.path, sys
os.chdir(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print >> sys.stderr, sys.path
import StringIO
_stdin = sys.stdin
sys.stdin = StringIO.StringIO('')

import web
from web import form

from imdb import IMDb
imdb = IMDb()

import imdbintersect

urls = (
    '/', 'search',
    '/intersect', 'intersect',
)

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
render = web.template.render('templates/', base='layout')

search_form = form.Form(form.Textbox('a', description='Search 1:'),
                        form.Textbox('b', description='Search 2:'),
                        validators=[
                            form.Validator('Must supply 2 search terms', lambda i: i.a and i.b)
                        ])

select_form = form.Form(form.Dropdown('a', description='Search 1:', args=[]),
                        form.Dropdown('b', description='Search 2:', args=[]))

class search:
    def GET(self):
        my_search = search_form()
        return render.search(my_search)

    def POST(self):
        my_search = search_form()
        if not my_search.validates():
            return render.search(my_search)
        else:
            my_select = select_form()
            my_select['a'].args = imdbintersect.simple_search(imdb, my_search['a'].value)
            my_select['b'].args = imdbintersect.simple_search(imdb, my_search['b'].value)
            return render.select(my_select)

class intersect:
    def GET(self):
        my_select = select_form()
        if my_select.validates():
            people = imdbintersect.intersect([imdb.get_movie(my_select['a'].value),
                                              imdb.get_movie(my_select['b'].value)])
            return render.display(imdb, people)

if __name__ == '__main__':
    app.run()
