from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent code injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', ' ', '_'])
    return run_ping(safe_host)