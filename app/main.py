from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    # Sanitize the host input to avoid command injection
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}