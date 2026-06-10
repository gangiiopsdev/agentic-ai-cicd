from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    args = ['ping', quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)