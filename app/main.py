from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, host))