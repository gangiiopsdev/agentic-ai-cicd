from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Check if host contains malicious characters
    if any(char in host for char in [';', '&', '|', '(', ')']):
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a whitelist of allowed hosts or use a safe method to validate the input
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'another-example.com']  # Populate this list with allowed hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)