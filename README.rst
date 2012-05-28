imdbintersect - intersect movie casts
=====================================

**This project is redundant - it turns out IMDb actually created this
feature back in February 2010, 7 months before I did.  I attribute this
duplication to the very low visibility of the feature and the fact that
I'd been considering creating this project for about 2 years previously.
Use the official tool here: http://www.imdb.com/search/common.**

A tool for finding out who has been in all of a set of movies.  Useful for
those times where you want to confirm a suspicion that you recognise somebody
in a movie, you don't know who they are, but you know something else they've
been in.

There are 3 parts: a library containing the intersection algorithm, a
command-line script for performing searches, and a web.py_ web application.

Command-line script
-------------------
::

    python imdbintersectcli.py SEARCH1 SEARCH2 ...

The command-line script should be run with at least 2 searches as arguments.
The user is then prompted to select a match for each term, and the results of
the intersection of the movie casts are displayed.

Web application
---------------
``imdbintersectweb.py`` is a normal web.py_ web application, and therefore
can be deployed just the same.  For now at least, it needs to be at the root
of the host, since the forms use absolute URLs (``/search`` etc.)  The demo
site is at http://imdbintersect.dev.hexi.co/.

Library
-------
``imdbintersect.py`` contains the main ``intersect`` algorithm, plus other
useful things.  The source is documented, read it!

Known issues
------------

* For some reason, movie search results are messed up when running the webapp through mod_wsgi, but 
  not when running the CLI or standalone web.py app, on the same machine with the same code.


.. _web.py: http://webpy.org/
