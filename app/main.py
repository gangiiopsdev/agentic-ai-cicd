from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping/{host}')
def read_ping(host: str):
    return ping(host)