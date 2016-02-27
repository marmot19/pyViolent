import socket
from warnings import catch_warnings
# 变量
port=21
banner = "FreeFloat FTP Server"
portList = [21, 22, 80, 110]
portOpen = True
print ("[+] Checking for " + banner + "on port " + str(port))
# print (type(banner))
# print (type(port))
# print (type(portList))
# print (type(portOpen))
# print (banner.find('FTP'))
# portList.append(5)
# portList.sort()
# print (portList)
pos = portList.index(80)
print ("[+] There are " + str(pos) + " ports to scan before 80.")
services = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}
# print (services.keys())
# print (services.items())
# print ('ftp' in services)
# print (services['ftp'])
print ("[+] Found vuln with FTP on port " + str(services['ftp']))
###### python socket测试，本地防火墙、FTP服务都打开，还是连不上？###
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("127.0.0.1", 21))
    ans = s.recv(1024)
    print (ans)
except Exception as e:
    print ("[-] Error = " + str(e))
##### python Exception 异常处理 #####
try:
    print (1370/0)
#     3.0版本后没有 except Exception, e的用法,显示语法错误
except Exception as e:
    print ("[-] Error = " + str(e))
# function  函数的使用
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return str(e)
def main():
    ip1 = "192.168.95.148"
    ip2 = "192.168.95.149"
    port = 21
    banner1 = retBanner(ip1, port)
    banner2 = retBanner(ip2, port)
    if banner1:
        print ("[+] " + ip1 + " :" + banner1 )
    if banner2:
        print ("[+] " + ip2 + " :" + banner2 )

if __name__ == '__main__':
    main()
