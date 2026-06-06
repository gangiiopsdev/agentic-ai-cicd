from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input to prevent injection attacks
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if any(char not in allowed_chars for char in host):  # Simplified validation
        return {'status': 'error', 'message': 'Invalid characters in host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)