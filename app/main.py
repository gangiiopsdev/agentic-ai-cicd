from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get('/ping')
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input
        if not request.host.isalnum():
            raise ValueError("Invalid input")
        args = ['ping', request.host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': str(e)}