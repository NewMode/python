from requests import request
import os
import json
import logging

logger = logging.getLogger(__name__)

API_URL = "https://engage.newmode.net/api/"


class Client(object):
    """
    Instantiate Client Class

    Args:
        api_user:
            The username to use for the API requests. Not required if ``NEWMODE_API_URL``
            env variable set.
        api_password:
            The password to use for the API requests. Not required if ``NEWMODE_API_PASSWORD``
            env variable set.
        api_version:
            The api version to use. Defaults to v1.0
    Returns:
        NewMode Class
    """

    def __init__(self, api_user=None, api_password=None, api_version='v1.0'):

        self.api_url = os.getenv('NEWMODE_API_URL', API_URL)
        self.api_user = os.getenv('NEWMODE_API_USER', api_user)
        self.api_password = os.getenv('NEWMODE_API_PASSWORD', api_password)
        self.api_version = os.getenv('NEWMODE_API_VERSION', api_version)

    def baseRequest(self, endpoint, method='GET', payload={}, supports_version=True, requires_csrf=True, params={}):
        # Internal Request Method

        url = self.api_url
        if supports_version:
            url += self.api_version + '/'

        url += endpoint

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
        response = self.baseRequest('session/token', 'GET', {}, False, False)
        if (response.status_code == 200):
            data = response.json()
            return data['X-CSRF-Token']
        else:
            logging.warning("Error getting CSRF Token")

        return None

    def getTools(self, params = {}):
        response = self.baseRequest('tool', 'GET', params = params)
        if (response.status_code == 200):
            return response.json()['_embedded']['hal:tool']
        else:
            logging.warning("Error getting tools")

    def getTool(self, tool_id, params = {}):
        response = self.baseRequest('tool/' + str(tool_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting tool")

    """
    Lookup targets for a given tool

    Args:
        tool_id:
            The tool to lookup targets.
        search:
            The search criteria. It could be:
            - Empty: If empty, return custom targets associated to the tool.
            - Postal code: Return targets matched by postal code.
            - Lat/Long: Latitude and Longitude pair separated by '::'.
              Ex. 45.451596::-73.59912099999997. It will return targets
              matched for those coordinates.
            - Search term: For your csv tools, this will return targets
              matched by given valid search term.
        params:
            Query params for request.
    Returns:
        Targets information.
    """

    def lookupTargets(self, tool_id, search=None, params = {}):
        endpoint = 'lookup/' + str(tool_id)
        if (search): 
            endpoint += '/' + search
        response = self.baseRequest(endpoint, params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error looking up for targets")

    """
    Get action information.

    Args:
        tool_id:
            The tool to retrieve.
    Returns:
        Action information including structure to run the action.
    """

    def getAction(self, tool_id, params = {}):
        response = self.baseRequest('action/' + str(tool_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting action")

    """
    Run specific action

    Args:
        tool_id:
            The tool to run.
        payload:
            The data to post to run the action.
            This data structure will depend on what has been
            returned by getAction.
    Returns:
        Posted outreach information.
    """

    def runAction(self, tool_id, payload, params = {}):
        response = self.baseRequest('action/' + str(tool_id), 'PATCH', json.dumps(payload), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error running action")

    def getTarget(self, target_id, params = {}):
        response = self.baseRequest('target/' + str(target_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting target")

    def getCampaigns(self, params = {}):
        response = self.baseRequest('campaign', params = params)
        if (response.status_code == 200):
            return response.json()['_embedded']['hal:campaign']
        else:
            logging.warning("Error getting campaigns")

    def getCampaign(self, campaign_id, params = {}):
        response = self.baseRequest('campaign/' + str(campaign_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting campaign")

    def getOrganizations(self, params = {}):
        response = self.baseRequest('organization', params = params)
        if (response.status_code == 200):
            return response.json()['data']
        else:
            logging.warning("Error getting organizations")

    def getOrganization(self, organization_id, params = {}):
        response = self.baseRequest('organization/' + str(organization_id), params = params)
        if (response.status_code == 200):
            return response.json()['data']
        else:
            logging.warning("Error getting organization")

    def getServices(self, params = {}):
        response = self.baseRequest('service', params = params)
        if (response.status_code == 200):
            return response.json()['_embedded']['hal:service']
        else:
            logging.warning("Error getting services")

    def getService(self, service_id, params = {}):
        response = self.baseRequest('service/' + str(service_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting service")

    def getOutreaches(self, tool_id, params = {}):
        params['nid'] = str(tool_id)
        response = self.baseRequest('outreach', params = params)
        if (response.status_code == 200):
            return response.json()['_embedded']['hal:outreach']
        else:
            logging.warning("Error getting outreaches")

    def getOutreach(self, outreach_id, params = {}):
        response = self.baseRequest('outreach/' + str(outreach_id), params = params)
        if (response.status_code == 200):
            return response.json()
        else:
            logging.warning("Error getting outreach")