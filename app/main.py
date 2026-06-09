from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to avoid command injection
    if not all(c.isalnum() or c in ("", "-") for c in host):
        return {'error': 'Invalid hostname'}
    subprocess.call([os.path.join("/sbin", "ping"), host])
    return {'status': 'completed'}