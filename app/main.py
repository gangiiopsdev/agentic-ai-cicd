from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing it to the subprocess
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)