from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in globally_safe_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    subprocess.call(['ping', '--'], input=b'')  # Add input parameter to prevent command injection
    return {'status': 'completed'}