from owlready import *
import types

games = Ontology("http://test.org/games.owl")
onto_path.append("C:/Users/ishara/Desktop/project")

games.load()
# NewClass = types.new_class("NewGamesClass", (Thing,), kwds = { "ontology" : games })
print(games.classes)
