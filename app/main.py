from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host name')
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {'status': 'completed'}