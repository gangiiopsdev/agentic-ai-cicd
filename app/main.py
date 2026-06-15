from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.Popen
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Example validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts