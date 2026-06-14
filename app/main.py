from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return host.strip().replace(' ', '_')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}