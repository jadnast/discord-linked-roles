store = {}

# A class for storing data, it is better not to change if you do not know what you are doing.

class storage():
    # Creating Data to Write to a Dictionary
    def store_discord_tokens(user_id, tokens):
        store[f'discord-{user_id}'] = tokens
    
    # Getting data from a dictionary
    def get_discord_tokens(user_id):
        return store.get(f'discord-{user_id}')