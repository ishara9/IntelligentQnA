from owlready import *
import types

class OntologyMaker:
# def mainM():
    ont_url = "http://www.semanticweb.org/intel.owl"
    # ont_url = "http://test.org/intel.owl"
    local_path = "C:/Users/ishara/Desktop/project/ontologies"
    onto = Ontology(ont_url)
    onto_path.append(local_path)
    ontoName = str(onto.load())


    # print(onto.dataTypeClassTester)

    mainClasses = ['Disease','Cure','Cause','Prevention','Symptom','Treatment']
    mainProperties = [['dataProp','Disease','Prevention'],['has_cause','Disease','Symptom']]

    classifiedWords = [['influenza','Disease'],['HIV','Disease'],['arthritis','Disease'],['immune_system_dysfunction','Symptom']]

    relationshipSet = [['arthritis','has_cause','immune_system_dysfunction']]



    def ClassDefiner(mainClasses,onto,ontoName):
        for eachclass in mainClasses:
            className = str(ontoName+"."+eachclass)
            if className.lower() not in str(onto.classes).lower():

                NewClass = types.new_class(eachclass, (Thing,), kwds={"ontology": onto})
                print("New Class Created "+eachclass)

    def PropertyDefiner(mainProperties,onto,ontoName):
        for eachRelation in mainProperties:
            relationName = str(ontoName + "." + eachRelation[0])
            if relationName.lower() not in str(onto.properties).lower():
                NewClass = types.new_class(eachRelation[0], (Property,), kwds={"ontology": onto })
                # types.prepare_class(eachclass, )
                # , body = {"domain": [eachRelation[1]], "range": [eachRelation[2]]}
                print("New Relation Created " + eachRelation[0])


    def updateClassifications(classifiedWords,onto,ontoName):
        for eachWord in classifiedWords:
            eachWordName = str(ontoName + "." + eachWord[0])
            if eachWordName.lower() not in str(onto.instances).lower():
                for thisClass in onto.classes:
                    if eachWord[1] == str(thisClass):
                        eachWord[0] = thisClass(eachWord[0])
                        print('New Instance Created ' + str(eachWord[0]))
        print('updateClassifications')

    def relationshipBuilder(relationshipSet,onto,ontoName):


        print("relationshipBuilder Executed")
        for eachRelation in relationshipSet:
            eachRelationName = str(ontoName + "." + eachRelation[0])
            for thisInstance in onto.instances:
                if eachRelation[0] == str(thisInstance):
                    print("eachRelation 0 "+ str(eachRelation[0]))
                    subject = thisInstance
                if eachRelation[2] == str(thisInstance):
                    print("eachRelation 2 " + str(eachRelation[2]))
                    object = thisInstance
            for thisProperty in onto.properties:
                if eachRelation[1] == str(thisProperty):
                    print("eachRelation 1 " + str(eachRelation[1]))
                    predicate = thisProperty
                    print(predicate)
                    # predicate.append(object)

            method = str(predicate)
            getattr(subject, method).append(object)

            # subject.has_cause.append(object)




        # my_drug.has_for_ingredient.append(acetaminophen)
        print()


    updateClassifications(classifiedWords,onto,ontoName)
    ClassDefiner(mainClasses,onto,ontoName)
    PropertyDefiner(mainProperties,onto, ontoName)
    relationshipBuilder(relationshipSet,onto,ontoName)
    # print(onto.classes)
    print(onto.properties)
    print(onto.instances)

    print(onto.TestProperty.range)

    # onto.save()

    # def Relation(onto):
    #
    #     class Drug(Thing):
    #         ontology = onto
    #
    #     class Ingredient(Thing):
    #         ontology = onto
    #
    #     class has_for_ingredient(Property):
    #         ontology = onto
    #         domain = [Drug]
    #         range = [Ingredient]


            # my_drug = Drug("my_drug")
            # acetaminophen = Ingredient("acetaminophen")
            # my_drug.has_for_ingredient.append(acetaminophen)



    # Test works FINE! :D


    # test_class = onto.TestClass
    # test_range_class = onto.TestRangeClass

    # testInstance = test_class("testInstance")
    # testRangeInstance = test_range_class("rangeSetter")
    # onto.testInstance.dataTypeClassTester.append(testRangeInstance)
    # onto.sync_reasoner()

    # print(test_class)


# mainM()