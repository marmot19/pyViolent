'''
Created on 2016年3月4日

@author: bpm-citic
'''

import optparse
from _socket import AF_INET, SOCK_STREAM, socket

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect(tgtHost, tgtPort)
        print ('[+] %d/tcp open'% tgtPort)
        connSkt.close()
    except:
        print '[-] %d/tcp closed'% tgtPort 
def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -P <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    if (tgtHost == None) | (tgtPort == None):
        print (parser.usage)
        exit(0)
    

if __name__ == '__main__':
    main()
    pass