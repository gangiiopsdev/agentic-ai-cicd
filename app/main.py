from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):