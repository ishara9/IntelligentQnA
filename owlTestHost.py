import owlReady
from owlReady import *

ont_url = "http://www.semanticweb.org/intel.owl"
# ont_url = "http://test.org/intel.owl"
# local_path = "C:/Users/ishara/Desktop/project/pyNew/ontologies"

owlready_ontology = get_ontology("http://localhost/onto/intel.owl").load()
print(owlready_ontology.python_name)
# onto = Ontology(ont_url)
# onto_path.append(owlready_ontology)
# ontoName = str(onto.load())
