from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    # Sanitize the input to prevent command injection
    sanitized_host = ''.join(filter(str.isalnum, request.host))
    result = subprocess.run(['ping', f'"{sanitized_host}"'], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}