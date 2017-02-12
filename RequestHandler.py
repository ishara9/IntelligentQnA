
import json
import urllib.request
import urllib.parse
import requests
import nltk
import re
import demjson

str1 = 'Ishara is 24 years old'
str2 = 'Ishara hasAge 24'
str3 = 'flu viruses are spread mainly by droplets'
str4 = 'droplets spreads flu viruses mainly'
headers = { 'Content' : 'text/plain' }

#print status POST request
r = requests.post("http://localhost:7777/", data=str3 , headers = headers)

print(r.status_code, r.reason)
print(r.text)

jsonObject = json.loads(r.text)

root = jsonObject[0]['tree']
nextLevel1 = ""
nounPhrases = []
verbPhrases = []
numbers = []

#Format -> jasonObject[0]['tree']["RootNode"][loopIndex]['tree']...
level1 = jsonObject[0]['tree']['ROOT'][0]['tree']

print(root)
print()

def treeSystem(root):

    for rootObj in root:
        print(rootObj)
        for num in range(0, len(root[rootObj])):
            print(
                "Index : " + str(root[rootObj][num]['index']) + ", POS : " + root[rootObj][num]['pos'] + ", Label : " + root[rootObj][num]['label'] + ", Token : " +
                root[rootObj][num]['token'])
            if(root[rootObj][num]['label']=='NOUN'):
                nounPhrases.append(root[rootObj][num]['token'])
            if (root[rootObj][num]['label'] == 'VERB'):
                verbPhrases.append(root[rootObj][num]['token'])
            if (root[rootObj][num]['label'] == 'NUM'):
                numbers.append(root[rootObj][num]['token'])
            print()

            #continute to nextLevel of the parse tree if such exists
            if 'tree' not in root[rootObj][num]:
                 continue
            nextLevel1= root[rootObj][num]['tree']
            treeSystem(nextLevel1)


treeSystem(root)
print(nounPhrases)
print(verbPhrases)
print(numbers)

#### Referencing Old code pure LOGIC####
# for rootObj in root:
#     print(rootObj)
#     for num in range(0, len(root[rootObj])):
#         print("Index : " + str(root[rootObj][num]['index']) + ", POS : " + root[rootObj][num]['pos'] + ", Token : " + root[rootObj][num]['token'])
#         print()
#
# for i in level1:
#     print("----"+i)
#     for num in range(0, len(level1[i])):
#         # print(len(jsonObject[0]['tree']['ROOT'][0]['tree'][i]))
#         print("----"+"Index : "+str(level1[i][num]['index'])+", POS : "+level1[i][num]['pos'] + ", Token : "+level1[i][num]['token'])
#         print()
#         if 'tree' not in jsonObject[0]['tree']['ROOT'][0]['tree'][i][num]:
#             continue
#         level2 = jsonObject[0]['tree']['ROOT'][0]['tree'][i][num]['tree']
#         for j in level2:
#             print("--------"+j)
#             for num2 in range(0, len(level2[j])):
#                 print("--------"+"Index : "+str(level2[j][num2]['index'])+", POS : "+level2[j][num2]['pos'] + ", Token : "+level2[j][num2]['token'])
#                 print()