> ❇️ This version is running successfully. If you need help, please [contact us](https://discord.gg/KHyUgCJYYK) :)

# Linked Roles
This repository is the non official discord repository rewritten for python, for a linked role bot.
- [official repository](https://github.com/discord/linked-roles-sample/)

## Project structure
All of the files for the project are on the left-hand side. Here's a quick glimpse at the structure:

```
├── images -> Images for documentation
├── modules
│   ├── discord.py  -> Discord specific auth & API wrapper
│   ├── storage.py  -> Provider for storing OAuth2 tokens
├── config.py  -> Parsing of local configuration
├── main.py  -> Main entry point for the application
├── register.py  -> Tool to register the metadata schema
├── requirements.txt  -> All libraries you need to install
└── README.md
```

## Running app locally

Before you start, you'll need to [create a Discord app](https://discord.com/developers/applications) with the `bot` scope

Configuring the app is covered in detail in the [tutorial](https://github.com/jadnast/discord-linked-roles/wiki/Configuring-App-Metadata-for-Linked-Roles).

### Setup project

First clone the project:
```
git clone https://github.com/jadnast/discord-linked-roles.git
```

Then navigate to its directory and install dependencies:
```
cd discord-linked-roles
pip install -r requirements.txt
```

### Get app credentials

Fetch the credentials from your app's settings and add them to a `config.py` file. You'll need your bot token (`DISCORD_TOKEN`), client ID (`DISCORD_CLIENT_ID`), client secret (`DISCORD_CLIENT_SECRET`). You'll also need a redirect URI (`DISCORD_REDIRECT_URI`) and a randomly generated UUID (`COOKIE_SECRET`), which are both explained below:

```
DISCORD_CLIENT_ID: <your OAuth2 client Id>
DISCORD_CLIENT_SECRET: <your OAuth2 client secret>
DISCORD_TOKEN: <your bot token>
DISCORD_REDIRECT_URI: https://<your-project-url>/discord-oauth-callback
COOKIE_SECRET: <random generated UUID> - already created
```

For the UUID (`COOKIE_SECRET`), we use:

```
uuid.uuid4().hex
```

### Running your app

After your credentials are added, you can run your app:

```
python main.py
```

And, just once, you need to register you connection metadata schema. In a new window, run:

```
python register.py
```
