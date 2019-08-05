# WhPy

[![PyPI](https://img.shields.io/pypi/v/WhPy)](https://pypi.org/project/WhPy/)
[![PyPI - License](https://img.shields.io/pypi/l/WhPy)](https://pypi.org/project/WhPy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/WhPy)](https://pypi.org/project/WhPy/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/WhPy)](https://pypi.org/project/WhPy/)

Python 3 webhook module for interacting with various chat applications via established webhooks.

## Installation

> pip install WhPy

## Code Examples

Hello, World!
``` python 3
from WhPy import discord

# Discord Webhook URL
webhook_url = "https://discordapp.com/api/webhooks/1234/567890"

# Creates Discord Instance
hook = discord.Webhook(url=webhook_url)

# Sets Message Content
hook.message(content="Hello, World!")

# Executes the Webhook
hook.execute()
```

Hello, World! from user `MichaelCduBois`
``` python 3
from WhPy import discord

# Discord WebHook Parameters
webhook_channel_id = "1234"
webhook_token = "567890"

# Creates Discord Instance
hook = discord.Webhook(channel_id=webhook_channel_id, token=webhook_token)

# Sets Message Content as MichaelCduBois
hook.message(content="Hello, World!", username="MichaelCduBois")

#Executes the Webhook
hook.execute()
```