from modules.discord import discord
from modules.storage import storage

import uuid

from flask import Flask, make_response, redirect, request

app = Flask(__name__)
state = str(uuid.uuid4())

@app.route('/')
def hello_world():
    return '👋'

@app.route('/verified-role')
def verified_role():
    res = make_response()
    url = discord.get_oauth_url()
    res.set_cookie('clientState', state)
    return redirect(url)

@app.route('/discord-oauth-callback')
def discord_oauth_callback():
    try:
        code = request.args.get['code']
        discord_state = request.args.get['state']

        client_state = request.cookies.get['clientState']
        if client_state != discord_state:
            print('State verification failed.')
            return redirect('/',code=403)

        tokens = discord.get_oauth_tokens(code)
        me_data = discord.get_user_data(tokens)
        user_id = me_data['user']['id']

        storage.store_discord_tokens(user_id, tokens)
        update_metadata(user_id)
        return 'You did it!  Now go back to Discord.'
    except Exception as e:
        print(e)
        return redirect('/',code=500)

@app.post('/update-metadata')
def update_metadata():
    try:
        user_id = request.json['userId']
        update_metadata(user_id)

        return redirect('/',code=204)
    except Exception as e:
        return redirect('/',code=500)

def update_metadata(user_id):
    tokens = storage.get_discord_tokens(user_id)
    metadata = {}
    try:
        metadata = {
            'cookieseaten': 1483,
            'allergictonuts': False,
            'firstcookiebaked': '2003-12-20',
        }
    except Exception as e:
        print('Error fetching external data:' + e)
    discord.push_metadata(user_id, tokens, metadata)

if __name__ == '__main__':
    app.run(port='80',debug=True)