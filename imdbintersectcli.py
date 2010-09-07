from imdb import IMDb

from imdbintersect import *

if __name__ == '__main__':
    import sys

    imdb = IMDb()

    movies = list()

    for m in sys.argv[1:]:
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
