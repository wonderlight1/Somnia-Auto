# Somnia Bot 🚀

An advanced and adaptable automation solution for the **Somnia Network**, offering a wide array of features to streamline testnet activities.

**TUTORIAL LINK:** [nelnabr.gitbook.io/auto-labs/somnia/somnia-eng](https://nelnabr.gitbook.io/auto-labs/somnia/somnia-eng)

## 🌟 Key Features

- ✨ Multi-threaded execution
- 🔁 Automatic retry system with customizable attempts
- 🛡️ Proxy support for anonymity and security
- 📊 Select specific account ranges
- ⏱️ Randomized delays between actions
- 📩 Telegram log integration
- 📃 Comprehensive transaction logging
- 🔧 Modular task-based architecture
- 🌐 Integration with Twitter and Discord
- 👥 Discord invite automation
- 💬 Blockchain messaging with Quills

## 🎯 Supported Actions

**Network Tools:**
- Access Somnia Faucet
- Transfer tokens
- Set user handles
- Retrieve account/network data
- Connect social profiles (Twitter, Discord)
- Participate in campaigns
- Invite via Discord

**Minting & NFT Operations:**
- Mint Ping Pong tokens
- Mint SHANNON NFT (Nerzo)
- Mint NEE NFT (Nerzo)
- Mint YAPPERS NFT (Alze)
- Mint SOMNI NFT (Mintaura)
- Deploy smart contracts (Mintair)

**Swapping & Messaging:**
- Token swaps (Ping Pong)
- Send blockchain-based messages via Quills

## 📋 System Requirements

- Python version `3.11.1` to `3.11.6`
- Wallet private keys (Somnia Network)
- Proxy list for secure access
- Twitter API tokens
- Discord bot/user tokens
- Messages for Quills

## 🚀 Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/neLNABR/Somnia.git
   cd Somnia
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration Steps:**
   - Edit `config.yaml`
   - Add wallet keys to `data/private_keys.txt`
   - Add proxies to `data/proxies.txt`
   - Add Twitter tokens to `data/twitter_tokens.txt`
   - Add Discord tokens to `data/discord_tokens.txt`
   - Add Quills messages to `data/random_message_quills.txt`

## 📁 Directory Overview

```
Somnia/
├── data/
│   ├── private_keys.txt
│   ├── proxies.txt
│   ├── twitter_tokens.txt
│   ├── discord_tokens.txt
│   └── random_message_quills.txt
├── src/
│   ├── modules/
│   └── utils/
├── config.yaml
└── tasks.py
```

## 📝 Configuration Guide

### 1. Input Data Files

- `data/private_keys.txt`: Private keys (one per line)
- `data/proxies.txt`: Proxies (`http://user:pass@ip:port`)
- `data/twitter_tokens.txt`: Twitter tokens (one per line)
- `data/discord_tokens.txt`: Discord tokens (one per line)
- `data/random_message_quills.txt`: Messages for Quills (one per line)

### 2. Main Configuration (`config.yaml`)

```yaml
SETTINGS:
  THREADS: 1
  ATTEMPTS: 5
  ACCOUNTS_RANGE: [0, 0]
  EXACT_ACCOUNTS_TO_USE: []
  SHUFFLE_WALLETS: true
  PAUSE_BETWEEN_ATTEMPTS: [3, 10]
  PAUSE_BETWEEN_SWAPS: [3, 10]
```

### 3. Module-Specific Settings

```yaml
SOMNIA_NETWORK:
  SOMNIA_SWAPS:
    BALANCE_PERCENT_TO_SWAP: [5, 10]
    NUMBER_OF_SWAPS: [1, 2]

  SOMNIA_TOKEN_SENDER:
    BALANCE_PERCENT_TO_SEND: [1.5, 3]
    NUMBER_OF_SENDS: [1, 1]
    SEND_ALL_TO_DEVS_CHANCE: 50

  SOMNIA_CAMPAIGNS:
    REPLACE_FAILED_TWITTER_ACCOUNT: false

  DISCORD_INVITER:
    INVITE_LINK: ""
```

## 🎮 Running the Bot

### Task Setup

Edit `tasks.py` to define which tasks to execute:

```python
TASKS = ["CAMPAIGNS"]
```

**Available Tasks:**
- `CAMPAIGNS`
- `FAUCET`
- `SEND_TOKENS`
- `CONNECT_SOCIALS`
- `MINT_PING_PONG`
- `SWAPS_PING_PONG`
- `QUILLS_CHAT`
- `SOMNIA_NETWORK_SET_USERNAME`
- `SOMNIA_NETWORK_INFO`
- `DISCORD_INVITER`

### Creating Custom Sequences

Example:

```python
TASKS = ["MY_CUSTOM_TASK"]

MY_CUSTOM_TASK = [
    "faucet",
    ("mint_ping_pong", "swaps_ping_pong"),
    ["nerzo_shannon", "nerzo_nee"],
    "quills_chat",
    "connect_socials",
    "discord_inviter"
]
```

### Launch Command

```bash
python main.py
```

## 📜 License

MIT License

## ⚠️ Disclaimer

This tool is intended for educational use only. Use responsibly and in accordance with relevant terms of service.
