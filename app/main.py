from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to prevent command injection
        if not request.host.isalnum() or '.' not in request.host:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        response = {
            'status': 'completed',
            'output': result.stdout
        }
        return jsonable_encoder(response)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}