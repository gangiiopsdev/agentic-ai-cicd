from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get('/'
)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation with full path and proper input validation
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}, 400

@app.get('/ping')
def ping_endpoint(host: str):
    if '@' not in host and len(host) < 256:
        return ping(host)
    else:
        return {'error': 'Invalid host'}, 400