from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, text=True, shell=False)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}