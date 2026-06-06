from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)