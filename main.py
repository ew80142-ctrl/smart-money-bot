import os

# Render will automatically inject your secrets into these lines
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# ... the rest of your trading bot code goes here ...
