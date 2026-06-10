from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host.strip() or any(c in host for c in [';', '&', '|', '$', '`']):
        return JSONResponse(status_code=400, content={'error': 'Invalid host input'})
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}