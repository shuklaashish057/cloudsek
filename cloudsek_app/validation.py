from rest_framework.exceptions import APIException
from rest_framework import status

class CustomValidation():
    def __init__(self):
        self.status_code = 204

    def get_and_validate(self, request_body):
        if len(request_body) <= 1:
            raise APIException("No Content, Request fulfilled, nothing follows", self.status_code)
