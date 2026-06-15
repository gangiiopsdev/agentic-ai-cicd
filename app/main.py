from fastapi import FastAPI
import subprocess
import shlex
global host_whitelist = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_whitelist:
        subprocess.call(['ping', shlex.quote(host)])  # Use shlex.quote to sanitize input
    else:
        return {'error': 'Host not allowed'}

    return {"status": "completed"}