from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from shlex import quote as cmd_quote

cmd = ['ping', '-c', '1', cmd_quote(host)]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host input')
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'result': result}