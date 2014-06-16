import requests
import json
mac = open('./csv/maclist.csv','r')
dev = open('./csv/devlist.csv','w')
for n in range(100):
    d=requests.get('http://aws.onion.io/ds/register/magic-mfg-key/'+mac.readline())
    dev.write(json.loads(d.text)['deviceId']+'\n')
dev.close()
mac.close()
