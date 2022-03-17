import requests

def kanye_quotes():
  apiResponse = requests.get('https://api.kanye.rest/')
  kanye = apiResponse.json()
  return kanye['quote']

def osrs_api():
  apiResponse = requests.get('https://api.osrsbox.com/monsters?where={ "name": "Troll", "duplicate": false }')
  osrsData = apiResponse.json()
  return osrsData

def apex_data(apexUsername):
  apiResponse = requests.get(f'https://api.mozambiquehe.re/bridge?platform=X1&player={apexUsername}&auth=Xib1lRSeP7JuOPSvxLg3')
  apexResponse = apiResponse.json()
  return apexResponse