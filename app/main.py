from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host or ' ' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)