from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

def secure_ping(host: str):
    if not host or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host name")
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)