import requests

print(requests.__version__)
r = requests.get('http://google.com')
print(r.status_code)