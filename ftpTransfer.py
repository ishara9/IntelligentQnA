import ftplib
import base64
import os
import codecs
import Owl2rdfConvc

filename = "beyond.owl"
#convert owl file into rdf format
x = Owl2rdfConvc.Owl2rdf(filename)

UID = "srilanakasquash"

key = open("../key.key","r")
byteCode = key.readline()
key.close()

enPass = codecs.decode(str.encode(byteCode),'hex').decode()

ftp = ftplib.FTP("66.206.41.137")
ftp.login(UID, enPass)
ftp.cwd("/public_html/srilankasquash.com/projects/onto")
os.chdir(r"C:\Users\ishara\Desktop\project\pyNew\ontologies")
myfile = open(filename, 'rb')
ftp.storlines('STOR ' + filename, myfile)
myfile.close()