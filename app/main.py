from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host: str):
    # Implement a more robust validation logic here, e.g., using regular expressions or a whitelist of allowed hosts.
    allowed_hosts = ['localhost', '127.0.0.1']
    return host.strip() in allowed_hosts