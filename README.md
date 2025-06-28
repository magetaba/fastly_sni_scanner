# 🔍 Fastly SNI Scanner for V2Ray REALITY

This project helps you dynamically scan and validate **Fastly CDN-backed domains and subdomains** to identify **clean SNI + IP pairs** that are compatible with **V2Ray REALITY protocol**.

It checks for:
- Valid DNS resolution
- Support for **TLS 1.3**
- Valid **SSL certificate** matching the SNI

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `fastly_sni_scanner.py` | Main Python script to scan Fastly domains for TLS 1.3 + valid SNI |
| `run_fastly_scanner.sh` | Bash script to set up Python virtual environment, install dependencies, and run the scanner |
| `fastly_source.txt` | List of candidate Fastly domains/subdomains (one per line) to scan |

---

## ⚙️ Requirements

- Python 3.7+
- `pip` for package installation

---

## 🚀 Usage

### 1. Clone the repo

```bash
git clone https://github.com/magetaba/fastly_sni_scanner.git
cd fastly_sni_scanner
```

### 2. Make the shell script executable

```bash
chmod +x run_fastly_scanner.sh
```

### 3. Run the script

```bash
./run_fastly_scanner.sh
```

This will:
- Create a Python virtual environment if not already created
- Install required dependencies: `requests` and `dnspython`
- Run the scanner and test domains listed in `fastly_source.txt`
- Save working results to `fastly_sni_working.txt`

---

## 📦 Example Output

```bash
Testing pbs.twimg.com → 151.101.1.91
 ✅ WORKS

🧾 Working SNI / IP results:
pbs.twimg.com → 151.101.1.91

📁 Saved 1 entries → fastly_sni_working.txt
```

---

## ✍️ How to Add More Domains

Edit `fastly_source.txt` and add one domain per line (no `https://` or slashes):

```txt
creators.spotify.com
pbs.twimg.com
slate.com
```

You can also include wildcards like `*.example.com` — the script will sanitize and parse them.

---

## 🤝 Credits

Developed by Magetaba → [@official_subzero](https://t.me/official_subzero)

If you find this useful, consider sharing or contributing!

---

## 🛡️ License

MIT License
