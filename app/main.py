from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping'] + [arg for arg in shlex.split(host) if arg.isalnum()]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)