from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid host name')
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}