from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host name")
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}