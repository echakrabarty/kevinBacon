The primary problem is the "6 degrees of Kevin Bacon".  The actor
Kevin Bacon has appeared in numerous movies, so it is reasonable to
find a path from an arbitrary film actor to Kevin Bacon within a few
movies.

Thus the party game among movie trivia experts is to come up with a
"Bacon Path", a series of movies and actors to go from the starting
actor to Kevin Bacon.  Thus, for example, Zoe Saldana appeared in
Guardians of The Galaxy along with Brendan Fehr, while Brendan Feir
was also in X-Men: First Class with Kevin Bacon. [1]

And yes, there is a wikipedia page:

https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon


The problem consists of 4 primary functions: loading the movie
database (in a .csv file) into a graph, doing a graph traversal to
come up with a minimum Bacon Path for an intended actor, a validation
function to validate that a path is a valid Bacon Path, and a
validation function to validate that a path is a minimum distance
Bacon Path.

