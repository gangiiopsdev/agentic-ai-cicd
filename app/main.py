from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def ping(request: PingRequest):
    try:
        # Sanitize the input to avoid shell injection
        sanitized_host = request.host.replace(';', '').replace('&', '').replace('|', '')
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.post('/ping')
def ping_post(request: PingRequest):
    return ping(request)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}