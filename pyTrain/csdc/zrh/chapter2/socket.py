'''
Created on 2016年3月4日

@author: bpm-citic
'''

import optparse
from threading import *
from _socket import AF_INET, SOCK_STREAM, socket, gethostbyname, gethostbyaddr,\
    setdefaulttimeout
import nmap

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect(tgtHost, tgtPort)
        connSkt.send('pyViolent\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print ('[+] %d/tcp open'% tgtPort)
        print ('[+] ' + str(results))
        
    except:
        screenLock.acquire()
        print ('[-] %d/tcp closed'% tgtPort )
    finally:
        connSkt.close()
        screenLock.release()

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print ('[*] ' + tgtHost + " tcp/" + tgtPort + " " + state)
    
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print ("[-] Cannot resovle '%s' : Unknown host"%tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("\n[+] Scan Result for: " + tgtName[0])
    except:
        print ("\n[+] Scan Result for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
#         print ("Scanning Port " + tgtPort)
        t = Thread(target=nmapScan, args=(tgtHost, tgtPort))
        t.start()
def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -P <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print (parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
    pass