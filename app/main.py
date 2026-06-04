from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic for host input
    return all(c.isalnum() or c in ['.', '-'] for c in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)