'''
Created on 2016年2月27日

@author: rongh
'''

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return str(e)

def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print ('[+] FreeFloat FTP Server IS vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print ('[+] 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print ('[+] Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print ('[+] Samin FTP Server is vulnerable.')
    else:
        print ('[+] FTP Server is not vulnerable.')

def checkVulnsF(banner):
    f = open('vlun_banners.txt', 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print ('[+] server is vulnerable: ' + banner.strip('\n') )
def main():
    portList = [20, 21, 25, 80, 110, 443]
    for x in range(0,4):
        ip = '192.168.95.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print ('[+] ' + ip +"-" + str(port) + ': ' + banner.strip('\n'))
                checkVulnsF(banner)
if __name__ == '__main__':
    main()
    pass