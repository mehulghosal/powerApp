import requests, zeep
import lxml.html
from getpass import getpass

user = input("username: ")
pasw = getpass()

def login():
    # GET parameters - URL we'd like to log into.
    LOGIN_URL = 'https://ps2.millburn.org/public/pearson-rest/services/PublicPortalServiceJSON?response=application/json'

    # Start session and get login form.
    session = requests.session()
    login = session.get(LOGIN_URL)

    # Get the hidden elements and put them in our form.
    login_html = lxml.html.fromstring(login.text)
    hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    # "Fill out" the form.
    form['username'] = input("username: ")
    form['password'] = input("password: ")

    # Finally, login and return the session.
    return session.post(LOGIN_URL, data=form)

def soap_test():
    soap_endpoint = "https://ps2.millburn.org/public/pearson-rest/services/PublicPortalService"
    url = "http://ps2.millburn.org/pearson-rest/services/PublicPortalService?wsdl"
    ur2 = "http://publicportal.rest.powerschool.pearson.com/xsd"
    wsse_auth = ["pearson", "pearson"]
    user = input("username: ")
    pasw = getpass()

    client = zeep.Client(ur2, wsse=wsse_auth)

    # login = client.create_message(client.message, "login", username=user, password=pasw, userType="Parent")
    return client

# import requests
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from zeep.transports import Transport
def another():
    url = "https://ps2.millburn.org/public/pearson-rest/services/PublicPortalService"
    ur2 = "http://publicportal.rest.powerschool.pearson.com/xsd"

    sess = Session()
    sess.auth = HTTPBasicAuth(user, pasw)

    client = zeep.Client(ur2, transport=Transport(session=sess))
    return client


if __name__ == '__main__':
    # login = soap_test()

    url = 'https://ps2.millburn.org/public/pearson-rest/services/PublicPortalServiceJSON?response=application/json'
    url2 = "http://sales.powerschool.com/pearson-rest/services/PublicPortalServiceJSON?wsdl"
    sess = Session()

    res = requests.post(url2, auth=HTTPDigestAuth(user, pasw))
    