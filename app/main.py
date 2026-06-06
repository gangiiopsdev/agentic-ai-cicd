from fastapi import FastAPI
import subprocess
import re
import shlex

global app
app = FastAPI()

def validate_host(host: str):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '4', safe_host], capture_output=True, text=True)
        return {'result': result.stdout}
    else:
        return {'error': 'Invalid host'}, 400