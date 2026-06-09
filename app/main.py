from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if '||' in v or '&' in v or ';' in v or '`' in v or '$' in v:
            raise ValueError('Invalid characters detected in host input')
        return v

    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}