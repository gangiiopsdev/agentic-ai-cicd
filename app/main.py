from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def execute_ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not (host.replace('.', '', 3).isdigit() and '@' not in host) or len(host.split('.')) != 4:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except ValueError as e:
        return str(e)

@app.post('/ping')
def ping(request: PingRequest):
    # Sanitize and validate the input host parameter before executing the ping command
    if not all(char.isdigit() for char in host) or len(host.split('.')) != 4:
        raise ValueError('Invalid host format')
    return execute_ping(host)