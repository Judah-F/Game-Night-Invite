import os
import requests

def send_instant_message():
    # Grab the URL from the GitHub Action environment
    webhook_url = os.environ.get('DISCORD_HOOK')

    if not webhook_url:
        print("❌ Error: Could not find DISCORD_HOOK in environment variables.")
        return

    # Data to send
    data = {
        "content": "🐍 **Python Test:** The bridge is active! This message was sent via Python inside a GitHub Action."
    }

    # Execute the POST request
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("✅ Success! Message delivered to Discord.")
        else:
            print(f"⚠️ Discord returned an error: {response.status_code}")
    except Exception as e:
        print(f"❌ Python Error: {e}")

if __name__ == "__main__":
    send_instant_message()
