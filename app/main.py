from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the input to prevent injection attacks
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)