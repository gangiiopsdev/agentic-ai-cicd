from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    validated_host = shlex.quote(request.host)
    result = subprocess.run(['ping', '-c', '1', validated_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get('/ping')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}