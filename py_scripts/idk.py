from requests.auth import HTTPDigestAuth
from requests import Session
from zeep import Client, exceptions
from zeep.transports import Transport
from zeep.settings import Settings

class PowerschoolAPI:
    def __init__(self, url, api_username:str = 'pearson', api_password:str = 'm0bApP5'):
        self.url_ = url
        self.session_ = Session()
        self.session_.auth = HTTPDigestAuth(api_username, api_password)
        self.api_username_ = api_username
        self.api_password_ = api_password
        self.setup()

    def setup(self):
        public_portal_service_url = self.url_ + '/pearson-rest/services/PublicPortalServiceJSON'
        settings = Settings(strict=False, raw_response=True, forbid_dtd=False, forbid_entities=False, forbid_external=False, xsd_ignore_sequence_order=True)
        self.client_ = Client(wsdl=public_portal_service_url + '?wsdl', transport=Transport(session=self.session_), settings=settings)


    def login(self, username, password):
        print(self.client_.service.loginToPublicPortal(username, password))
        #print(self.client_.loginToPublicPortal(username, password))


    url_ = None
    session_ = None
    api_username_ = None
    api_password_ = None
    client_ = None

api = PowerschoolAPI('http://sales.powerschool.com', 'pearson', 'm0bApP5')