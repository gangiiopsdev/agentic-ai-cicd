from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host input is sanitized to avoid injection attacks
    if any(char in host for char in [';', '&', '|', '`']):
        raise ValueError('Invalid characters in hostname')
    result = subprocess.run(['ping'], capture_output=True, text=True, args=[host])
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)