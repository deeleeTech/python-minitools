import requests

def kanye_quotes():
  apiResponse = requests.get('https://api.kanye.rest/')
  kanye = apiResponse.json()
  return kanye['quote']