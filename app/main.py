from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize hostname using a regular expression
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', shlex.quote(host)]  # Use list and shlex.quote to avoid shell=True and mitigate injection risk
    subprocess.run(args, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}