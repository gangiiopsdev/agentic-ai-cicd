from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):\n    try:\n        output = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}\n    except Exception as e:\n        return {'status': 'failed', 'error': str(e)}