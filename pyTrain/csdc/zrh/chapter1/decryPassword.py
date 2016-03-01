'''
Created on 2016年2月29日

@author: rongh
'''
import hashlib

def testPass(cryptPass):
    salt = cryptPass[0:2]
    salt_bypte = salt.encode('utf-8')
    print ("原密码: " + cryptPass)
    dictFile = open('dictionary.txt', 'r')
    for line in dictFile.readlines():
        word = line.strip('\n')
        word_byte = word.encode('utf-8')
        cryptWord = hashlib.sha512(word_byte)
#         cryptWord.update(word_byte)
        print ("字典加密后密码： " + cryptWord.hexdigest())
        if cryptWord == cryptPass:
            print ("[+] Found Password: " + word + '\n')
            return
    print ("[-] Password not Found.\n")
    return
def main():
    file = open('password.txt', 'r')
    for line in file.readlines():
        if ":" in line :
            user = line.split(":")[0]
            password = line.split(":")[1].strip(' ')
            print ("[+] Cracking password for " + user )
            testPass(password)
if __name__ == '__main__':
    main()
    pass