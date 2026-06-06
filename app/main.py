from fastapi import FastAPI
import subprocess
import shlex
import re

def safe_ping(host):
    try:
        # Sanitize input using regular expression
        if not re.match(r'^[a-zA-Z0-9]+$', host):
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)