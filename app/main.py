from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}