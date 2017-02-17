from nltk.corpus import wordnet as wn
import _pickle

class WordIdentifier:
    synslist = []
    def synsetCreate(self,listClass,trainingList):
        listClassName ='identitiy/'+str(listClass)+'.p'
        print(trainingList)
        synslist = []
        for w in trainingList:
            for syn in wn.synsets(w):
                synslist.append(str(syn))
        _pickle.dump(synslist, open(listClassName, 'wb'))

    def synsetUpdate(self,listClass,trainingList):
        listClassName ='identitiy/'+str(listClass)+'.p'
        print(trainingList)
        for w in trainingList:
            for syn in wn.synsets(w):
                self.synslist.append(str(syn))
        _pickle.dump(self.synslist, open(listClassName, 'wb'))

    def loadSynlist(self,listClass):
        listClassName = 'identitiy/' + str(listClass) + '.p'
        self.synslist = _pickle.load(open(listClassName, 'rb'))

    def identifyClass(self,wordToIdentify):
        hypernamepaths = []
        for syns in wn.synsets(wordToIdentify):
            for hypset in syns.hypernym_paths():
                for hyp in hypset:
                    hypernamepaths.append(str(hyp))

        commonTerms = filter(lambda w: w in self.synslist, hypernamepaths)
        return len(set(commonTerms)) > 0

    # list = ['disease','illness','cancer','contamination','defect','disorder','epidemic','fever','flu','illness']
    # #list = ['disease','illness','cancer','contamination','defect','disorder','epidemic','illness']
    # list =[]
    # _pickle.dump(list, open('list2.p', 'wb'))
    # list = _pickle.load(open('list3.p', 'rb'))
    # synslist =_pickle.load(open('list3.p', 'rb'))

    # print(list)
    # for w in list:
    #     for syn in wn.synsets(w):
    #         synslist.append(str(syn))

    # print(synslist)
    # _pickle.dump(synslist, open('list3.p', 'wb'))
    # synslist = _pickle.load(open('list3.p', 'rb'))

    # def checkDisease(self,disease):
    #     hypernamepaths =[]
    #     for syns in  wn.synsets(disease):
    #         for hypset in syns.hypernym_paths():
    #             for hyp in hypset:
    #                 hypernamepaths.append(str(hyp))
    #
    #     commonTerms = filter(lambda w:  w in self.synslist,hypernamepaths)
    #     return len(set(commonTerms))>0

wordIdentifier = WordIdentifier()

list = ['disease','illness','cancer','contamination','defect','disorder','epidemic','fever','flu','illness']
wordIdentifier.synsetCreate("disease",list)
wordIdentifier.loadSynlist("disease")
print (wordIdentifier.identifyClass("Heart_attack"))

