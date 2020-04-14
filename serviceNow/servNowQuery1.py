import requests

# Setup request
url = 'https://myinstance.service-now.com/api/now/table/incident?sysparm_limit=10'
user = 'kjeffreys@lhric.org'
pwd = 'Jflwin100@'

# Setup headers
headers = {'Accept' : 'application/json'}

# Perform HTTP request
resp = requests.get(url, auth=(user,pwd), headers=headers)

# Check for 200 okay code
if respon
