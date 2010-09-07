def simple_search(imdb, search):
    """Get search results as ``(id, title)`` pairs."""
    return [(m.getID(), m['long imdb title']) for m in imdb.search_movie(search)]

def intersect(movies):
    """Intersect the casts of a list of movies.

    Intersect the casts of each movie in *movies*, finding those actors that
    are present in all of them.  It is assumed that each movie has had it's
    cast data fetched (e.g. by using ``imdb.update(m, 'cast')``).
    
    Returns data in the following structure:
    
        [(person, [(movie, [role,
                            role,
                            ...]),
                   (movie, [role,
                            ...])]),
         (person, [...]),
         ...]
    """
    assert(len(movies) > 0)
    # Build datastructure for cast lookup
    movie_lookup = dict((m.getID(), m) for m in movies)
    cast_lookup = dict((m.getID(), dict((p.getID(), p) for p in m['cast'])) for m in movies)
    # Start with the first movie's cast
    s = set(cast_lookup[movies[0].getID()].keys())
    # Intersect with all other movies
    s = s.intersection(*(cast_lookup[m.getID()].keys() for m in movies[1:]))
    
    people = list()
    for p in s:
        appearsin = list()
        for m in movies:
            person = cast_lookup[m.getID()][p]
            appearsin.append((m, person.currentRole))
        people.append((cast_lookup[movies[0].getID()][p], appearsin))

    return people


def select_candidate(search, candidates):
    """Command-line prompt to select a search result.

    A search for a movie might give several results.  This prompts the user to
    choose one result from *candidates*.
    """
    print "Search for '%s' returned multiple results:" % (search,)
    for i, m in enumerate(candidates):
        print "\t%d\t%s" % (i, m['long imdb title'])
    print "\ti\t[Ignore this search]"

    while True:
        choice = raw_input("Enter an option: ")
        
        if choice == 'i':
            return None
        
        try:
            choice = int(choice)
            if choice < len(candidates):
                return candidates[choice]
        except ValueError:
            # Falls through to prompting again
            pass

        print "Option '%s' not recognised" % (choice,)
