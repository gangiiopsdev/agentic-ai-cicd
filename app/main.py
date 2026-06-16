from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}