from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Safe implementation using subprocess.run
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic regex to validate host
        raise ValueError('Invalid host format')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'output': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}