from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input here
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

# Helper function to validate host
def is_valid_host(host: str) -> bool:
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))