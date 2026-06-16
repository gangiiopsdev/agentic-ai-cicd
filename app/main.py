from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}