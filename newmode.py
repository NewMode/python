from requests import request
import os
import json
import logging

logger = logging.getLogger(__name__)

API_URL = "https://engage.newmode.net/api/"


class Newmode(object):
    """
    Instantiate Newmode Class

    `Args:`
        user_email:
            The email of the API user for Copper. Not required if ``COPPER_USER_EMAIL``
            env variable set.
        api_key:
            The Copper provided application key. Not required if ``COPPER_API_KEY``
            env. variable set.
    `Returns:`
        NewMode Class
    """

    def __init__(self, api_user=None, api_password=None, api_version=None):

        self.api_url = os.getenv('NEWMODE_API_URL', API_URL)
        self.api_user = os.getenv('NEWMODE_API_USER', api_user)
        self.api_password = os.getenv('NEWMODE_API_PASSWORD', api_password)
        self.api_version = os.getenv('NEWMODE_API_VERSION', api_version)

    def baseRequest(self, endpoint, params={}, payload={}, method='GET', supports_version=True, requires_csrf=False):
        # Internal Request Method

        url = self.api_url
        if supports_version:
            url += self.api_version + '/'

        url += endpoint

        # Authentication must be done through headers, requests HTTPBasicAuth doesn't work
        headers = {
            'Content-Type': "application/json"
        }
        if (requires_csrf):
            csrf = self.getCSRFToken()
            headers["X-CSRF-Token"] = csrf

        # GET request with non-None data arg is malformed
        response = None
        if method == 'GET':
            response = request(method, url, params=params, headers=headers, auth=(self.api_user, self.api_password))
        else:
            response = request(method, url, params=params, data=payload, headers=headers, auth=(self.api_user, self.api_password))

        return response

    def getCSRFToken(self):
        response = self.baseRequest('session/token', {}, {}, 'GET', False, False)
        if (response.status_code == 200):
            data = response.json()
            return data['X-CSRF-Token']

        return None

    def getTools(self):
        response = self.baseRequest('tool', {}, {}, 'GET', True, True)
        print(response.status_code)
        if (response.status_code == 200):
            return response.json()['_embedded']['hal:tool']

    def getTool(self, tool_id):
        response = self.baseRequest('tool/' + str(tool_id), {}, {}, 'GET', True, True)
        print(response.status_code)
        if (response.status_code == 200):
            return response.json()
