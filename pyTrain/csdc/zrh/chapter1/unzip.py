#coding=utf-8
''''
Created on 2016年3月1日

@author: rongh
'''
import zipfile
import optparse
from threading import Thread
def zipExtract(zFile, password):
    try:
        #     zipfile带密码解压时，注意密码需先进行UTF-8编码
        zFile.extractall(pwd=password.encode('utf-8'))
        print ("[+] Found password " + password + '\n')
        return password
    except:
        pass
    
def main():
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=zipExtract, args=(zFile, password))
        t.start()
if __name__ == '__main__':
    main()
    pass