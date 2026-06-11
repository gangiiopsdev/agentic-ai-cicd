from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement sanitization logic here (e.g., whitelist of allowed hosts)
    return '127.0.0.1'  # Placeholder for actual implementation

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}