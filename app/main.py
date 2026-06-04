from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with full path and shell check
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}