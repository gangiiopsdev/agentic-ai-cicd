from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if any(char in host for char in [';', '&', '|']):
        return {'status': 'failed', 'error': 'Invalid input'}
    # Use a whitelist of allowed hosts or implement more robust validation
    allowed_hosts = ['127.0.0.1', '::1']  # Example: allow only localhost
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)