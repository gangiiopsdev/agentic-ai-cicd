from fastapi import FastAPI
import subprocess
import shlex
import re

def execute_ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not re.match(r'^\d{1,3}(?:\\.\d{1,3}){2}\\.\d{1,3}$', host) or len(host.split('.')) != 4:
        raise ValueError('Invalid IP address')
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=False, input=safe_host)
    return {'status': 'completed' if result.returncode == 0 else 'error', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)