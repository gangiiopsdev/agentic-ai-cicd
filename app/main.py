from fastapi import FastAPI
import subprocess
generics = ['icmp', 'udp', 'tcp']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in generics:
        subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid protocol')
    return {"status": "completed"}