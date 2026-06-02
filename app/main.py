from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', *shlex.split(request.host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}