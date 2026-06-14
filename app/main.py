from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.strip() or ' ' in host or '\t' in host:
        return {'error': 'Invalid input'}
    # Sanitize the host input further to ensure it does not contain any unexpected characters or paths
    sanitized_host = subprocess.list2cmdline(host.split())
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}