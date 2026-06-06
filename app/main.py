from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid input'}

    call = subprocess.run(['ping', host], capture_output=True, text=True)
    result = call.stdout if call.returncode == 0 else call.stderr
    return {'status': 'completed', 'result': result}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)