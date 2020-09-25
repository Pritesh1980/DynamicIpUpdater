import logging
import urllib.request
import os.path
from os import path
import json
import requests

# logging.basicConfig(filename='/root/dns-updates.log',level=logging.INFO)
logging.basicConfig(
    filename='/root/dns-updates.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

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
    with open('creds.json') as creds_file:
        data = json.load(creds_file)
        # print(data)
        url = data['url']
        apikey = data['api-key']

        print("URL: " + url)
        print("Api-Key: " + apikey)

        # Issue GET request
        r = requests.get(url, headers={"x-api-key":apikey})
        logging.debug(r)

        logging.info("DNS updated to " + currentIp)


def main():
    if( external_ip_changed() ): 
        updateDns()
    else:
        logging.debug("IP unchanged")




if __name__=="__main__":
    main()
