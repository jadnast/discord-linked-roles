import requests
import json

import config 

url = f'https://discord.com/api/v10/applications/{config.DISCORD_CLIENT_ID}/role-connections/metadata'
body = [
  {
    'key': 'cookieseaten',
    'name': 'Cookies Eaten',
    'description': 'Cookies Eaten Greater Than',
    'type': 2,
  },
  {
    'key': 'allergictonuts',
    'name': 'Allergic To Nuts',
    'description': 'Is Allergic To Nuts',
    'type': 7,
  },
  {
    'key': 'bakingsince',
    'name': 'Baking Since',
    'description': 'Days since baking their first cookie',
    'type': 6,
  },
]

response = requests.put(url, data=json.dumps(body), headers={
  'Content-Type': 'application/json',
  'Authorization': f'Bot {config.DISCORD_TOKEN}',
})
if response.ok:
  data = response.json()
  print(data)
else:
  data = response.text
  print(data)