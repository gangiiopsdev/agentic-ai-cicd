from fastapi import FastAPI
import subprocess
cimport os

global app = FastAPI()

def ping(host: str):
    try:
        # Validate host to prevent injection
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)