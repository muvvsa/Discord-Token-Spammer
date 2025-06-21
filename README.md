
# ☠️ Discord Token Spammer by Anielka 😈

A simple yet ruthless terminal-based Discord token spammer. Load multiple tokens and blast messages to any channel on repeat – just for *educational* purposes, of course. 😏

---

## 🚀 Features

- 📦 Multi-token support (from `token.txt`)
- 💬 Customizable message + channel input
- ⏱️ Configurable delay between token actions
- 🧼 Terminal cleaner for cross-platform support
- 🖥️ ASCII splash screen to flex your terminal

---

## ⚙️ How It Works

1. Loads tokens from `token.txt` (one per line).
2. Takes user input for:
   - Channel ID
   - Message content
   - Delay between token sends
3. Iteratively sends the message to the given channel using all tokens.
4. Runs indefinitely like a true spam engine.

---

## 📁 File Structure

```
main.py         # The core script  
token.txt       # Your tokens (1 per line)
```

---

## 🛠️ Requirements

- Python 3.x  
- `requests` module  
  Install via: `pip install requests`

---

## 🧪 Usage

```bash
python main.py
```

Then follow the prompts:

- Input Channel ID  
- Type the message you want to spam  
- Set your delay (in seconds)

---

## 🧨 Example Output

```
📺 Channel ID to spam: 123456789012345678
💬 Message to send: I am unstoppable 😈
⏱️ Delay between tokens (in sec): 0.5

🚀 Spamming...

✅ Sent from token ending with XyZ123
✅ Sent from token ending with AbC789
❌ Failed (403) - token ending with PoW456
```

---

## ⚠️ Legal Disclaimer

> This tool is for **educational purposes only**.  
> Using this on servers or tokens without permission may violate Discord’s Terms of Service.  
> You are solely responsible for how you use this code.

---

## 🐾 Made with chaos and cats by Anielka 💜

> *“Why just exist when you can dominate the logs?”*
