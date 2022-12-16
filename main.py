import uuid
from modules.discord import discord
from modules.storage import storage
from flask import Flask, make_response, redirect, request

# Main HTTP server used for the bot.

app = Flask(__name__)
app.secret_key = b"random bytes representing flask secret key"
state = str(uuid.uuid4())

# Just a happy little route to show our server is up.
@app.route('/')
def hello_world():
    return '👋'

@app.route('/linked-roles', methods = ['POST', 'GET'])
@app.route('/verified-role', methods = ['POST', 'GET'])
def verified_role():
    res = make_response()
    url = discord.get_oauth_url()
    res.set_cookie('clientState', state)
    return redirect(url)

# Route configured in the Discord developer console, the redirect Url to which
# the user is sent after approving the bot for their Discord account. This
# completes a few steps:
# 1. Uses the code to acquire Discord OAuth2 tokens
# 2. Uses the Discord Access Token to fetch the user profile
# 3. Stores the OAuth2 Discord Tokens in Redis / Firestore
# 4. Lets the user know it's all good and to go back to Discord
@app.route('/discord-oauth-callback', methods = ['POST', 'GET'])
def discord_oauth_callback():
    # 1. Uses the code to acquire Discord OAuth2 tokens
    code = request.args['code']

    tokens = discord.get_oauth_tokens(code)

    # 2. Uses the Discord Access Token to fetch the user profile
    me_data = discord.get_user_data(tokens['access_token'])
    user_id = me_data['user']['id']
    storage.store_discord_tokens(user_id, tokens)

    # 3. Update the users metadata
    update_metadata(user_id)

    return 'You did it!  Now go back to Discord.'

# Given a Discord UserId, push static make-believe data to the Discord 
# metadata endpoint. 
def update_metadata(user_id):
    # Fetch the Discord tokens from storage
    tokens = storage.get_discord_tokens(user_id)
    metadata = {}
    try:
        # Fetch the new metadata you want to use from an external source. 
        # This data could be POST-ed to this endpoint, but every service
        # is going to be different.  To keep the example simple, we'll
        # just generate some random data. 
        metadata = {
            'cookieseaten': 3000,
            'allergictonuts': False,
            'firstcookiebaked': '2003-12-20',
        }
    except Exception as e:
        print('Error fetching external data:' + e)
        # If fetching the profile data for the external service fails for any reason,
        # ensure metadata on the Discord side is nulled out. This prevents cases
        # where the user revokes an external app permissions, and is left with
        # stale linked role data.

    # Push the data to Discord.
    discord.push_metadata(user_id, tokens, metadata)

# Normal launch of Flask application
if __name__ == '__main__':
    app.run(port='80',debug=True) # if you want to change port, host.. You can do it this!