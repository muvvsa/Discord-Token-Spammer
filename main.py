import requests as req
import time as t
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def load_tokens():
    path = "token.txt"
    if not os.path.exists(path):
        print("❌ token.txt not found!")
        return []

    with open(path, "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()]
    return tokens

def send_message(token, channel_id, message):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "content": message
    }
    r = req.post(f"https://discord.com/api/v10/channels/{channel_id}/messages",
                      headers=headers, json=payload)

    if r.status_code == 200:
        print(f"✅ Sent from token ending with {token[-6:]}")
    else:
        print(f"❌ Failed ({r.status_code}) - token ending with {token[-6:]}")


def run():
    cls()
    l = r"""
     __  ___                       ___ 
    /  |/  /_  ___   ___   _______/   |
   / /|_/ / / / / | / / | / / ___/ /| |
  / /  / / /_/ /| |/ /| |/ (__  ) ___ |
 /_/  /_/\__,_/ |___/ |___/____/_/  |_|
    TOKEN SPAMMER ☠️ by Anielka 😈
    """
    width = os.get_terminal_size().columns
    for line in l.splitlines():
        print(line.center(width))

    tokens = load_tokens()
    if not tokens:
        input("No tokens found. Press Enter to exit...")
        return

    channel_id = input("📺 Channel ID to spam: ")
    message = input("💬 Message to send: ")
    try:
        delay = float(input("⏱️ Delay between tokens (in sec): "))
    except ValueError:
        delay = 1.0

    print("\n🚀 Spamming...\n")

    while True:
        for token in tokens:
            send_message(token, channel_id, message)
            t.sleep(delay)

if __name__ == "__main__":
    run()
