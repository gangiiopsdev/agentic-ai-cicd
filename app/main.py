from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

def execute_ping(host: str):
    try:
        safe_host = cmd_quote(host)
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    return execute_ping(host)

# Helper function to validate host input
def is_valid_host(host: str) -> bool:
    import re
    pattern = r'^([a-zA-Z0-9.-]+)$'  # Simplified regex for demonstration
    return re.match(pattern, host) is not None