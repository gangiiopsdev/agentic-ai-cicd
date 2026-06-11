from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent injection
    if not all(c.isalnum() or c in '.-!' for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)