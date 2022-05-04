import config.config
import utility
from utility.utility_methods import *
from config.config import *
import pytest
import requests
import json
import sys
from cerberus import Validator

class Test_001:

    util_obj = Utility()
    get_url = base_url+get_request_path
    post_url = base_url+post_request_path
    put_url= base_url+put_request_path
    patch_url = base_url+patch_request_path
    delete_url = base_url+delete_request_path

    def test_get_user_list(self):
        for x in get_request_id_list:
            final_get_url = self.get_url+str(x)
            response = self.util_obj.user_details_get(final_get_url)
            print(response.status_code)
            response_json = response.json()
            #print(response_json)
            assert response.status_code == 200, "Invalid status code, Failed:"
            assert response_json['page'] == 2, "Number of pages does not match"
            assert response_json['total'] == 12, "Total not matching"
            assert response_json['data'][0]['email']== "michael.lawson@reqres.in" , "Email ID does not match"
            #print(response.headers)


    def test_create_user_post(self):
        response = self.util_obj.create_user_post(self.post_url)
        print(response.status_code)
        assert response.status_code == 201, "Invalid status code"
        response_json = response.json()
        print(response_json)
        assert response_json['name'] == "Vishwa", "Invalid name"
        assert response_json['job'] == "Automation", "Job not matching"

    def test_update_user_put(self):
        response = self.util_obj.update_user_put(self.put_url)
        print(response.status_code)
        assert response.status_code == 200, "Invalid status code"
        response_json = response.json()
        #print(response_json)
        assert response_json['name'] == "Vishwa", "Name not matching"


    def test_update_user_patch(self):
        response = self.util_obj.update_user_patch(self.patch_url)
        print(response.status_code)
        assert response.status_code == 200, "Invalid status code"
        response_json = response.json()
        assert response_json['job'] == "Automation", "Name not matching"


    def test_delete_user(self):
        response = self.util_obj.user_delete(self.delete_url)
        print(response.status_code)
        assert response.status_code == 204, "Invalid status code"



