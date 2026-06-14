from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run with shell=False and list arguments
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        return {'error': 'Invalid IP address'}, 400
    return {'status': safe_ping(host)}