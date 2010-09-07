# imdbintersect - intersect movie casts
#
# Copyright (c) 2010, Alan Briolat
# MIT licensed - see LICENSE

import sys

from imdb import IMDb

from imdbintersect import *

def main(args):
    if len(args) == 0:
        print "usage: python imdbintersectcli.py SEARCH1 SEARCH2 ..."
        return

    imdb = IMDb()
    movies = list()

    for m in args:
        candidates = imdb.search_movie(m)
        movie = select_candidate(m, candidates)

        if movie:
            movies.append(movie)

    movies = map(lambda m: imdb.get_movie(m.getID()), movies)

    people = intersect(movies)

    for person, movies in people:
        print '%s (%s)' % (unicode(person), imdb.get_imdbURL(person))
        for movie, roles in movies:
            print '\t%s: %s' % (unicode(movie), roles)


if __name__ == '__main__':
    main(sys.argv[1:])
