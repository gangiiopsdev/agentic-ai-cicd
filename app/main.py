from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        response = {
            'status': 'completed',
            'output': result.stdout
        }
        return jsonable_encoder(response)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}