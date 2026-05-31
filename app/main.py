from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return False, None
    return True, host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    is_valid, validated_host = validate_host(host)
    if not is_valid:
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', validated_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}