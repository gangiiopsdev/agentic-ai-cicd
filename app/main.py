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
        # Sanitize the input to avoid command injection
        sanitized_host = subprocess.list2cmdline(args[1:])
        result = subprocess.run(['ping'] + [sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}