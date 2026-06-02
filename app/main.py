from fastapi import FastAPI
import subprocess

def escape_host(host):
    return host.replace('\', '/').replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Secure implementation using a safe method to avoid command injection
    subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {"status": "completed"}