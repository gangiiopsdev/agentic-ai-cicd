from fastapi import FastAPI
import subprocess
import shlex
g from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Validate the input to ensure it does not contain unexpected characters or patterns that could lead to injection attacks.
    if not request.host.isdigit():
        return {'error': 'Invalid host parameter'}, 400

    args = shlex.split(f'ping {request.host}')
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500