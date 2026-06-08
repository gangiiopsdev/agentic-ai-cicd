from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    call_args = ['ping', host]
    result = subprocess.run(call_args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)