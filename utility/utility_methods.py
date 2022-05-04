import json

import requests
import testdata
class Utility:

    def user_details_get(self,url):
        response = requests.get(url)
        return response


    def create_user_post(self, url):
        file = open("./testdata/data.json","r")
        mydata = file.read()
        payload = json.loads(mydata)
        response = requests.post(url,data=payload)
        return response

    def update_user_put(self, url):
        file = open("./testdata/data.json","r")
        mydata = file.read()
        payload=json.loads(mydata)
        response = requests.put(url,data=payload)
        return response


    def update_user_patch(self,url):
        file = open("./testdata/data.json","r")
        mydata = file.read()
        payload = json.loads(mydata)
        response = requests.patch(url, data=payload)
        return response

    def user_delete(self, url):
        response = requests.delete(url)
        return response
