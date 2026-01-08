import datetime
import os
#from googleapiclient.discovery import build
from discord_webhook import DiscordWebhook


# Grab the secret from the environment
webhook_url = os.environ.get('DISCORD_WEBHOOK')

if not webhook_url:
    print("Error: DISCORD_WEBHOOK environment variable not found!")
else:
    print("Webhook found. Ready to send message.")
webhook = DiscordWebhook(url=webhook_url, content="Hello World!")
response = webhook.execute()
