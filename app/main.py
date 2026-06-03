from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize user input
        if not request.host.isalnum():
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', f'-c 4 {request.host}'], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}