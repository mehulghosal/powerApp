import requests
import getpass as gp
from bs4 import BeautifulSoup


USERNAME = input("enter your username: ")
PASSWORD = gp.getpass("enter your pass: ")
url = "https://ps2.millburn.org/pearson-rest/services/PublicPortalService?"
ur1 = "https://ps2.millburn.org//pearson-rest/services/PublicPortalServiceJSON?response=application/json"

# actType = "Parent"

# r = requests.post(ur1, auth=(user, pw))

# print(r.content)

def get_Auth():

    # USERNAME = User.get("1.0", END)
    # PASSWORD = Pass.get("1.0", END)
    # print(USERNAME)
    # print(PASSWORD)

    url = 'https://ps2.millburn.org/public/home.html'

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.92 Safari/537.36 Vivaldi/1.6.689.34'}

    g = requests.get(url)

    soup = BeautifulSoup(g.content)

    # 'Find The Values'

    PSTOKEN = None
    CONTEXTDATA = None

    for input in soup.find_all('input')[0:1]:
        PSTOKEN = input.get('value')

        # print(PSTOKEN)

    for input in soup.find_all('input')[1:2]:
        CONTEXTDATA = input.get('value')

        # print(CONTEXTDATA)


    payload = {
              'pstoken': PSTOKEN,
              'contextData': CONTEXTDATA,
              'dbpw': '',
              'translator_username': '',
              'translator_password': '',
              'translator_ldappassword': '',
              'returnUrl': 'https://ps2.millburn.org/public/home.html',
              'serviceName': 'PS Parent Portal',
              'serviceTicket': '',
              'pcasServerUrl': '\ /',
              'credentialType': 'User Id and Password Credential',
              'account': USERNAME,
              'pw': PASSWORD,
              'translatorpw': ''
              }

    r = requests.post(soup, data=payload)
    # print(r)

get_Auth()

#AGHHHWRGWRGWRGIOHWEUICNJWNCJN