#!/usr/bin/env python3

import sys
import csv


import graph
import json


class Baconator():

    def __init__(self, filename):
        

        self.bacongraph = graph.Graph()
        with open(filename, 'r') as file:
            baconFile = csv.reader(file)
            for row in baconFile:
                for i in row:
                    if i in self.bacongraph:
                        continue
                    else:
                        self.bacongraph[i] = i
                movie = row[0]
                actors = row[1:]
                for actor in actors:
                    self.bacongraph.connect(actor, movie)
                    self.bacongraph.connect(movie, actor)
            

    def find_min_baconpath(self, actor):
        """Returns a minimum length baconpath between the named actor
        and "Kevin Bacon", or None if no such path exists or if the
        actor is not found.
        """
        
        path = []
        if actor not in self.bacongraph:
            return None
        if actor == "Kevin Bacon":
            path.insert(0,actor)
        for bacon in self.bacongraph.bfs_traversal(actor):
            if bacon.name == "Kevin Bacon":
                while bacon != None:
                    path.insert(0,bacon.name)
                    bacon=bacon.previous
        return path

    
    def is_baconpath(self, path):
        """A check to see if something is a valid Baconpath, but not
        necessarily a minimal baconpath"""
        if len(path)==1 and path[0]== "Kevin Bacon":
            return True
        if len(path) < 2:
            return False
        firstStep = path[0]
        for step in path:
            nextStep = path[path.index(step)-len(path)+1]
            if step == "Kevin Bacon" and nextStep == firstStep:
                break
            if step in self.bacongraph and nextStep in self.bacongraph and self.bacongraph.connected(step, nextStep):
                continue
            else:
                return False
            
        return True
            
    

    def is_min_baconpath(self, path):
        if len(path)==1 and path[0]== "Kevin Bacon":
            return True
        if not self.is_baconpath(path):
            return False
        if path == self.find_min_baconpath(path[0]):
            return True
        else:
            return False

    def gimme_20(self):
        """This should return a string that is a JSON object for an
        entry in the tests list
         """
        test_entry = {
            "name": "gimme 20",
            "score": 20,
            "max_score": 20
        }
        return json.dumps(test_entry)
if __name__ == "__main__":
    baconator = None
    if len(sys.argv) > 1:
        baconator = Baconator(sys.argv[1])
    else:
        baconator = Baconator("moviedata.csv")
    

    # Some basic sanity tests, since Meg Ryan only appeared in one
    # movie with Kevin Bacon we know this is the only valid minimum
    # baconpath.
    path = baconator.find_min_baconpath("Meg Ryan")
    baconator.is_baconpath(path)
    assert path == ['Meg Ryan', 'In the Cut', 'Kevin Bacon']
    #print(path)
    assert baconator.is_baconpath(path)
    assert baconator.is_min_baconpath(path)

    assert not baconator.is_baconpath(['Meg Ryan'])
    assert baconator.is_baconpath(['Meg Ryan', "You've Got Mail",
                                   "Tom Hanks", "Apollo 13", 'Kevin Bacon'])
    assert not baconator.is_min_baconpath(['Meg Ryan', "You've Got Mail",
                                           "Tom Hanks", "Apollo 13",
                                           'Kevin Bacon'])
    
    path[1] = "bogus"
    assert not baconator.is_baconpath(path)
    X = baconator.find_min_baconpath("Esha Chakrabarty")
    #print(X)
    Y = ['Kevin Bacon', 'In the Cut', 'Meg Ryan']
    print(baconator.is_baconpath(Y))
    print(baconator.is_min_baconpath(Y))
    print(baconator.find_min_baconpath("Nicholas Weaver"))
    print(baconator.is_min_baconpath(["Kevin Bacon"]))
    print(baconator.is_baconpath(["Kevin Bacon"]))
    Z = ['Kevin Bacon', 'In the Cut', 'Kevin Bacon']
    print(baconator.is_baconpath(Z))
    print(baconator.is_min_baconpath(Z))


