import requests
import getpass as gp

my_user = input("enter your username: ")
my_pass = gp.getpass("enter your pass: ")

url = "https://ps2.millburn.org/public/home.html"

response = requests.post(url, allow_redirects=False, data={
  'fieldAccount': my_user,  
  'fieldPassword': my_pass
  })

print(response)
print(response.content)