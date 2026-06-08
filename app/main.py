from fastapi import FastAPI
import subprocess
import shlex
import re
cimport re

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host input using a more restrictive regular expression
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        # Use shlex.quote for command arguments to prevent shell injection
        output = subprocess.run(['ping'] + [shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)