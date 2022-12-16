store = {}

class storage():
    async def store_discord_tokens(user_id, tokens):
        await store.set(f'discord-{user_id}', tokens)
    
    async def get_discord_tokens(user_id):
        return await store.get(f'discord-{user_id}')