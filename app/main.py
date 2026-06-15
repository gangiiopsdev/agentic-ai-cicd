from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and check=True
    if host.isnumeric() or all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        subprocess.run(['ping', host], check=True, shell=False)
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping_endpoint(host: str):    return ping(host)

@app.get("")
def home():    return {"message": "Agentic Self-Healing Pipeline"}