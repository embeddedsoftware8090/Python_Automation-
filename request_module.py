import requests
x = requests.get('https://velocity.in')
print(x.text)
print(x.cookies)

