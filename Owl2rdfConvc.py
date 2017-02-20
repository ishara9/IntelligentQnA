from subprocess import call
class Owl2rdf:
    def  __init__(self,ontology):
        # ontology = "beyond.owl"
        call(["convert.bat" ,"owl2rdfconvert/","Rdf2Owl2.jar","ontologies/"+ontology+""])
