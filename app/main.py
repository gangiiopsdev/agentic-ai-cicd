from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

@app.post("/ping")
def ping(request: BaseModel):
    if not request.get('host') or len(request['host']) > 255:
        raise ValueError('Invalid host name')
    args = ['ping', request['host']]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}