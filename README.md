# NetBank CTF – IDOR Challenge

This is a simple Flask-based CTF challenge that simulates a fake online banking system. It contains an **IDOR (Insecure Direct Object Reference)** vulnerability.

## 🕵️ Challenge

Users can log in and view their own account. However, there's an account ID in the URL which is not properly protected. By changing this ID, attackers can view other users' sensitive data, including the flag.

### 🧪 Example Accounts

- **Username:** `alice`  
  **Password:** `password123`  
- **Username:** `bob`  
  **Password:** `password123`

Once logged in, visit `/account?account_id=1001` or `/account?account_id=1002`.

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

Each user has a "flag" in their account info shown on the `/account` page.

## 📰 News

News items are loaded from the corresponding `news.json` file and displayed on the news page.

## 🛡️ Intended Exploit

Manipulate the `account_id` in the URL to access accounts that don't belong to you.

**Example:**
- Log in as Alice
- Visit `/account?account_id=1002`
- View Bob’s flag

Good luck!
