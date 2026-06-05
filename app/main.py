from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_secure(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}