# IntelligentQnA

Currently Ongoing Project. 

#Introduction

From a given context this system is able to abstract information and convert it to ontolgy based knowledge system. 
From that knowledge area any user can ask questions from the system in order to obtain most suitable answer by the system.

#Text to Ontology (Text mining approach)

Basic architecture of this part is to provide natural langauge based text to be converted into a ontology which then updated with new knowledge.

Benifit of having ontology is it allowes us to infer new knowledge from the existing knowledge.

#Tools required

1. [Parsey McParseface server](https://hub.docker.com/r/andersrye/parsey-mcparseface-server/) - which allowes to convert the sentences in natural language into parse trees.
Run this server locally to access api calls using HTTP POST requests.

2. [OwlReady](http://pythonhosted.org/Owlready/) which is python 3 based ontology manipulation tool.

install using py -m pip install owlready

3. NLTK tool kit which required to access WordNet synset module 
```python
>>>from nltk.corpus import wordnet as wn
>>>wn.synsets('flu', pos=wn.NOUN)
[Synset('influenza.n.01')]
```


