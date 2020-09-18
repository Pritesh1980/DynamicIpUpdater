import logging
import urllib.request
import os.path
from os import path


logging.basicConfig(filename='ip-changes.log',level=logging.INFO)

currentIp = None
storedIpFile = '/root/stored-ip'


def external_ip_changed():
    currentIp  = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(currentIp)
   
    if( not path.exists(storedIpFile) ):
        print(f"IP file {storedIpFile} does not exist")
    else:
        print("IP file exists")

  
def updateDns():
    pass 





def main():
    if( external_ip_changed() ):
        updateDns()





if __name__=="__main__":
    main()
