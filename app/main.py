from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Safe implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout if result.returncode == 0 else result.stderr}

app = FastAPI()

@app.get('/')</br>
def home():</br>
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')</br>
def ping_endpoint(host: str):</br>
    # Validate and sanitize input before passing to subprocess</br>
    if not all(c.isalnum() or c in '.-' for c in host):</br>
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)