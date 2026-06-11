from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = {'localhost', '127.0.0.1'}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return {'status': 'completed', 'output': result.stdout.decode()}