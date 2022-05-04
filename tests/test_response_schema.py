import requests
import json
from cerberus import Validator
from utility.utility_methods import *
from config.config import *
from cerberus import Validator
class Test_002:

    post_url= base_url+post_request_path
    schema = {
        "name": {'type': 'string'},
        "job": {'type': 'string'},
        "id": {'type': 'string'},
        "createdAt":{'type': 'string'}
    }
    util_obj = Utility()

    def test_post_response_schema(self):
        response = self.util_obj.create_user_post(self.post_url)
        user = json.loads(response.text)
        print(user)
        validator = Validator(self.schema)
        is_valid = validator.validate(user)
        assert is_valid == True, "Schema validation failed"