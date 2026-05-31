from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Use subprocess.run instead of subprocess.call for better security and more control
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return secure_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}