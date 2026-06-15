from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)

def validate_ip_address(ip_address):
    octets = ip_address.split('.').strip()
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    return True

def validate_domain_name(domain):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]{1,}$')
    if not pattern.match(domain):
        return False
    parts = domain.split('.')
    if len(parts) > 2:
        return False
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_ip_address(host) or validate_domain_name(host):
        sanitized_host = quote(host)
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host format"}