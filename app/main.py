from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with input validation and sanitization
    args = ['ping', '-c', '1', host]  # Limit the number of pings to 1 for safety
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation and sanitization
    if not host.isalnum() or '&&' in host or ';' in host:
        return {'status': 'error', 'output': 'Invalid host'}
    return safe_ping(host)