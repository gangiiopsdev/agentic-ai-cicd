from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host input
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts