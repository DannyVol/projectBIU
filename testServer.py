import requests
import json
import os
import time

address = os.popen("minikube kubectl -- get services --namespace default flask-service --output jsonpath='{.status.loadBalancer.ingress[0].ip}'").read()
body = {
    "Content-Type": "application/json",
    "content": "ping"
}

while True:
    pathUri = 'http://' + address + ':5005/pingpong'
    request = requests.get(pathUri, json=body, verify=False,)
    content = json.loads(request.text)
    print(str(pathUri) + str(content) + " Ding Dong digi dong my k8s very long...")
    time.sleep(5)
