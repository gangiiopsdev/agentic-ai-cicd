from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list instead of shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Add input validation to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}