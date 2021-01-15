import requests

print("requests library version: " + requests.__version__)
r = requests.get('http://google.com')
print("google.com status code: " + str(r.status_code))
r2 = requests.get('https://raw.githubusercontent.com/rcs-tringuyen/cmput404_lab1/main/print_requests_version.py?token=AKIOAYEGMW6FFABGPRH7WBDAAH4HQ')
print(r2.text)