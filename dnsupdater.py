import logging
import urllib.request
import os.path
from os import path


logging.basicConfig(filename='dns-updater.log',level=logging.INFO)

currentIp = None
storedIpFile = '/root/stored-ip'


def external_ip_changed():
    global currentIp  
    currentIp = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(currentIp)
   
    if( not path.exists(storedIpFile) ):
        logging.debug("IP file [{}] does not exist".format(storedIpFile))
        with open(storedIpFile, "w") as ip_file:
            ip_file.write(currentIp)
        return True
    else:
        print("IP file exists")
        with open(storedIpFile, "r") as ip_file:
            storedIp = ip_file.read()

        # Check if stored IP matches current external IP
        if( storedIp == currentIp ):
            print("IP Address unchanged")
            return False
        else:
            with open(storedIpFile, "w") as ip_file:
                ip_file.write(currentIp)
            return True



  

def updateDns():
    print("DNS Update requested for: " + currentIp) 



def main():
    if( external_ip_changed() ):
        updateDns()





if __name__=="__main__":
    main()
