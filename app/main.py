from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

allowed_hosts = {'google.com', 'example.com'}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ['ping', quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}