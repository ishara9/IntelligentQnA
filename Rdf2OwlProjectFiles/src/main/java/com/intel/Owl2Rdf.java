
package com.intel;
//import all necessary classes
import java.io.File;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.io.RDFXMLOntologyFormat;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyManager;


@SuppressWarnings("deprecation")
public class Owl2Rdf {

//create a main() function to take an argument; here in the example one argument only
  public static void main(String[] args) throws Exception {

      // Get hold of an ontology manager
      OWLOntologyManager manager = OWLManager.createOWLOntologyManager();

      // Load the ontology from a local files
      //File file = new File("C:/Users/ishara/Desktop/project/pyNew/ontologies/intelowl.owl");
      File file = new File(args[0]);
      System.out.println("Loaded ontology: " + file);
      OWLOntology ontology = manager.loadOntologyFromOntologyDocument(file);

      // save the file into RDF/XML format
      //in this case, my ontology file and format already manage prefix
      RDFXMLOntologyFormat rdfxmlFormat = new RDFXMLOntologyFormat();
      manager.saveOntology(ontology, rdfxmlFormat, IRI.create(file));
  }
}