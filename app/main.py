from fastapi import FastAPI
import subprocess
from shlex import quote
globally_allowed_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.call(['ping', '-c', '1', quote(host)], shell=False)  # Use specific options to minimize risk and sanitize input
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}