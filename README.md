# NetBank CTF – IDOR Challenge

This is a simple Flask-based CTF challenge that simulates a fake online banking system. It contains an **IDOR (Insecure Direct Object Reference)** vulnerability.

## 🕵️ Challenge

Users can log in and view their own account. However, there's an account ID in the URL which is not properly protected. By changing this ID, attackers can view other users' sensitive data, including the flag.

### Bank 1
Number - 1001
### Bank 2
Date - 20120518
### Bank 3
Tick - 1751372321
### Bank 4
base64 - MjAxMjA1MTg=
### Bank 5
SHA2-256 - b2c342eee7c7d70c70cda29309de5e4a22d2a3a539fc9859fa3ff0f2eff9bd47
### Bank 5
Brutforce hash



## 🚀 Running the App

### With Docker

```bash
docker build -t netbank-ctf .
docker run -p 5000:5000 netbank-ctf
```

Then go to [http://localhost:5000](http://localhost:5000)

### Without Docker

```bash
pip install -r requirements.txt
python app.py [bankname]
```

- If you run `python app.py bank1` it will use `accounts1.json` and `news1.json`.
- If you run `python app.py bank2` it will use `accounts2.json` and `news2.json`.
- Place your `accountsX.json` and `newsX.json` files in the same directory as `app.py`.

## 📍 Flag Locations

One account on the `/account` page has s flag.

## 📰 News

News items are loaded from the corresponding `news.json` file and displayed on the news page.

## 🛡️ Intended Exploit

