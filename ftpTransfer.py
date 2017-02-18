import ftplib
import base64
import os
import codecs

filename = "beyond.owl"
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