from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['127.0.0.1', '::1']  # Define allowed hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=403, detail='Forbidden')

    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}