from fastapi import FastAPI
import subprocess

global run
run = subprocess.run

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and logging
    if host in ['127.0.0.1', '::1']:  # Allow only local hosts for security reasons
        result = run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid or unauthorized host'}, 403