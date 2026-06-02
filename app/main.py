from fastapi import FastAPI
import subprocess

def validate_host(host: str) -> bool:
    # Simple validation logic
    allowed_hosts = ["example.com", "anotherdomain.com"]
    return host in allowed_hosts

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}