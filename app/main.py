from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    try:
        args = ['ping', request.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'response': result.stdout}
    except Exception as e:
        return {'error': str(e)}