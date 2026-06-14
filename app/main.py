from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
async def ping(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}