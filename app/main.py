from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
from shlex import quote as cmd_quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise HTTPException(status_code=400, detail='Host parameter is required')
    try:
        # Validate and sanitize the input
        safe_host = cmd_quote(host)
        result = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))