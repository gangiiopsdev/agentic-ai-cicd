from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)