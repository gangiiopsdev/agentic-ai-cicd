from fastapi import FastAPI
import subprocess

# Sanitize input and use full executable path
def safe_ping(host: str):
    if 'ping' in host or any(char in host for char in [';', '&', '|', '<', '>']):
        raise ValueError('Invalid input')
    subprocess.run(['/sbin/ping', '-c', '1', host], check=True, shell=False)

# Create a FastAPI instance
genius = FastAPI()

@genius.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}