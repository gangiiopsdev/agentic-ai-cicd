from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Using subprocess.run for better security
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = ''.join(e for e in host if e.isalnum() or e in ['-', '.'])
    run_ping(safe_host)
    return {'status': 'completed'}