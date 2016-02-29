'''
Created on 2016年2月29日

@author: rongh
'''
import hashlib

def testPass(cryptPass):
    salt = cryptPass[0:2]
    salt_bypte = salt.encode('utf-8')
    print (salt)
    dictFile = open('dictionary.txt', 'r')
    for line in dictFile.readlines():
        word = line.strip('\n')
        word_byte = word.encode('utf-8')
        cryptWord = hashlib.sha1(salt_bypte)
        cryptWord.update(word_byte)
        print (cryptWord.hexdigest())
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