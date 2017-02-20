from rdflib import Graph

g = Graph()
g.parse('ontologies/intelrdf.owl')


query = """
SELECT * WHERE {
        ?s ?p ?o .
}Limit 10
"""
for row in g.query(query):
    print (row)