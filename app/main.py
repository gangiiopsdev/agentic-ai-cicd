from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip().replace(' ', '')
    if not is_safe_hostname(safe_host):
        raise ValueError("Invalid hostname")
    subprocess.run(["ping", "/bin/ping", safe_host], check=True)
    return {"status": "completed"}

def is_safe_hostname(hostname: str) -> bool:
    # Basic validation of the hostname
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in hostname)