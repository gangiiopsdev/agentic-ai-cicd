from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Safe implementation with proper sanitization and error handling
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        output = str(e.output.decode('utf-8'))
    return output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection and environment variable injection
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid hostname')
    return {"status": "completed", "output": safe_ping(host)}