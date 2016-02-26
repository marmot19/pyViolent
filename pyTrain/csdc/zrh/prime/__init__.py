import socket
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
print ("There are " + str(pos) + " ports to scan before 80.")
services = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}
# print (services.keys())
# print (services.items())
# print ('ftp' in services)
# print (services['ftp'])
print ("[+] Found vuln with FTP on port " + str(services['ftp']))
socket.setdefaulttimeout(2)
s = socket.socket()

