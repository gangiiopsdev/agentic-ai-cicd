from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in valid_chars for char in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}