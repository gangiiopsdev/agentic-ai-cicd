from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

@app.get("/ping")
def ping_route(host: str):
    if len(host) > 255 or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)