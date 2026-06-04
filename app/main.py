from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Secure implementation
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')  # Basic input sanitization
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)