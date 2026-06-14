from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get('/ping')
def ping(request: PingRequest):
    try:
        args = ['ping', request.host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}