from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)