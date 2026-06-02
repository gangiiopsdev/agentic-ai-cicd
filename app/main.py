from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or host == 'localhost' or host.startswith('127.0.0.1'):
        return secure_ping(host)
    else:
        return {'status': 'error', 'error': 'Invalid host'}