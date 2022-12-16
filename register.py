import requests
import json
import config 

# Register the metadata to be stored by Discord. This should be a one time action.
# Note: uses a Bot token for authentication, not a user token.

url = f'https://discord.com/api/v10/applications/{config.DISCORD_CLIENT_ID}/role-connections/metadata'
# supported types: number_lt=1, number_gt=2, number_eq=3 number_neq=4, datetime_lt=5, datetime_gt=6, boolean_eq=7, boolean_neq=8
# You can read more here https://discord.com/developers/docs/resources/application-role-connection-metadata
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