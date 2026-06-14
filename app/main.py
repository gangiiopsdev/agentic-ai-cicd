from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or not host.strip():
        return {'status': 'failed', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)