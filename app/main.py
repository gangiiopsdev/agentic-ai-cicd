from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using list of arguments to prevent shell injection
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize user input to prevent shell injection
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid host name')
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}