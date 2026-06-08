from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):  
    # Sanitize the input to prevent command injection
    safe_host = subprocess.list2cmdline([request.host])  
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}