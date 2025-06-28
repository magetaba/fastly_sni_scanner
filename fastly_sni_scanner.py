import ssl, socket, subprocess, dns.resolver, requests, random, re

resolver = dns.resolver.Resolver()
resolver.lifetime = resolver.timeout = 2.0

def fetch_fastly_snis():
    print("📄 Reading Fastly SNIs from local file: fastly_source.txt")
    try:
        with open("fastly_source.txt", "r") as f:
            lines = f.readlines()
            domains = set()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    match = re.match(r"^[a-zA-Z0-9.-]+$", line)
                    if match:
                        domains.add(line)
        print(f"✅ Loaded {len(domains)} domains from file")
        return list(domains)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []

def resolve_ip(domain):
    try:
        return resolver.resolve(domain, 'A')[0].to_text()
    except:
        return None

def tls_ok(ip, domain):
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_3
    try:
        with socket.create_connection((ip,443), timeout=3) as s:
            with ctx.wrap_socket(s, server_hostname=domain):
                cert = s.getpeercert()
                sans = [e[1] for e in cert.get("subjectAltName", [])]
                return domain in sans
    except:
        return False

def tls_openssl(ip, domain):
    cmd = ["openssl","s_client","-connect",f"{ip}:443","-servername",domain]
    try:
        r = subprocess.run(cmd, input=b"", stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=7)
        out = r.stdout.decode()
        return "TLSv1.3" in out and "Verify return code: 0 (ok)" in out
    except:
        return False

def scan(limit=50):
    domains = fetch_fastly_snis()
    random.shuffle(domains)
    working = []
    tested = 0

    print(f"\n🔍 Scanning up to {limit} Fastly domains...\n")
    for d in domains:
        if tested >= limit:
            break
        ip = resolve_ip(d)
        if not ip:
            tested += 1
            continue
        print(f"Testing {d} → {ip}")
        if tls_ok(ip, d) or tls_openssl(ip, d):
            print(" ✅ WORKS")
            working.append((d, ip))
        else:
            print(" ❌ FAIL")
        tested += 1

    print("\n🧾 Working SNI / IP results:")
    for d, i in working:
        print(f"{d} → {i}")

    with open("fastly_sni_working.txt", "w") as f:
        for d, i in working:
            f.write(f"{d} {i}\n")
    print(f"\n📁 Saved {len(working)} entries → fastly_sni_working.txt")
    print(f"\nProudly made with ❤️  for all Iranians 🇮🇷")
    print(f"\n❄️  https://t.me/official_subzero 💙")

if __name__ == "__main__":
    scan(50)
