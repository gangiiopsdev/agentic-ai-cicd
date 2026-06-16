from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Sanitize the input to prevent command injection
        sanitized_host = subprocess.quote(request.host)
        result = subprocess.run(['ping', '-c 4', sanitized_host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}