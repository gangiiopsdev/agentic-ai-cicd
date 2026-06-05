from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
from starlette.exceptions import HTTPException

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = _sanitize_input(request.host)
    try:
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

def _sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())