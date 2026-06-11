from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    if 'localhost' in host or '127.0.0.1' in host:
        args = ['ping', '-c', '1', host]  # Limiting the number of pings for security
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else 'Ping failed'
    else:
        return 'Invalid host'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}