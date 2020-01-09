import requests, json
# from XML import XML
      
# request = json.dumps("""<?xml version="1.0" encoding="utf-8"?>
#               <soapenv:envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.webserviceX.NET/">
#                   <soapenv:header>
#                   <soapenv:body>
#                       <web:conversionrate>
#                           <web:fromcurrency>GBP</web:fromcurrency>
#                           <web:tocurrency>CHF</web:tocurrency>
#                       </web:conversionrate>
#                   </soapenv:body>
#               </soapenv:header></soapenv:envelope>""")
 
# # encoded_request = request.encode(encoding='utf-8')
 
# encoded_request = request
# headers = {"Host": "www.webservicex.net",
#            "Content-Type": "text/xml; charset=UTF-8",
#            "Content-Length": len(encoded_request)}
                           
# response = requests.post(url="http://www.webservicex.net/CurrencyConvertor.asmx",
#                          headers = headers,
#                          data = encoded_request)
#                          # verify=False)
                          
# # print unicode(XML(response.text))

# print(response)




# url="http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
# #headers = {'content-type': 'application/soap+xml'}
# headers = {'content-type': 'text/xml'}
# body = """<?xml version="1.0" encoding="UTF-8"?>
#          <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
#             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
#             <SOAP-ENV:Header/>
#               <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
#          </SOAP-ENV:Envelope>"""

# response = requests.post(url,data=body,headers=headers)
# print(response.content)


from suds.client import Client
url="http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
client = Client(url)
print client ## shows the details of this service

result = client.service.GetWeatherInformation() 
print result 