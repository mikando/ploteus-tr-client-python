import requests
from requests.auth import HTTPBasicAuth

class ploteus_client(object):

    def __init__(self, username, password):
        self.__username=username
        self.__password=password

    def __get_headers(self):
        return {'user-agent': 'ploteus-tr-python/0.0.1', 'Accept': 'application/xml'}

    def __get_auth(self):
        return HTTPBasicAuth(self.__username, self.__password)

    def __get_uri(self,path):
        return "https://ploteus.iskur.gov.tr/api/Ploteus/" + path

    def upload_learning_opportunities_xml(self, xml):
        headers = self.__get_headers()
        return requests.post(self.__get_uri('uploadLearningOpportunitiesXml'), timeout=600, data = xml.encode('utf-8'), headers=headers, auth=self.__get_auth())

    def upload_qualifications_xml(self, xml):
        headers = self.__get_headers()
        return requests.post(self.__get_uri('uploadQualificationsXml'), timeout=600, data = xml.encode('utf-8'), headers=headers, auth=self.__get_auth())

    def get_status(self, requestId):
        headers = self.__get_headers()
        parameters = {'requestId': requestId}
        return requests.get(self.__get_uri('getXmlStatus'), timeout=600, headers=headers, auth=self.__get_auth(), params=parameters)