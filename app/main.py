from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using list instead of string and validate input
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum() or len(host) > 255:
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'stdout': e.stdout, 'stderr': e.stderr}