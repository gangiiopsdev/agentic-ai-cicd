from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.isalnum() or len(host) > 255:
        return False
    allowed_hosts = ['example.com', 'another.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'error', 'output': 'Unauthorized host'}
    result = subprocess.run(['ping', '-c', str(4), '--'], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}