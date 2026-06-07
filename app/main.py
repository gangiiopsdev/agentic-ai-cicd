from fastapi import FastAPI
import subprocess
global ping_host_set
ping_host_set = set(['127.0.0.1', '::1'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ping_host_set:
        raise Exception('Invalid host')
    # Safe implementation using subprocess.run with shell=False and list arguments
    subprocess.call(['ping', host])
    return {"status": "completed"}