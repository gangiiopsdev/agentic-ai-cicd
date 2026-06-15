from fastapi import FastAPI
import subprocess
from pydantic import validator, constr

app = FastAPI()

class PingRequest:
    host: constr(max_length=255)

@app.post('/ping', response_model=dict)
async def ping(request: PingRequest):
    try:
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}