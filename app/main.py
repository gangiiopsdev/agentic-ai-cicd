from fastapi import FastAPI
import shlex
import subprocess

global_safe_hosts = {'example.com', '192.0.2.1'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in global_safe_hosts:
        return {'status': 'error', 'error': 'Unauthorized host'}
    try:
        cmd = ['ping', *shlex.split(host)]
        output = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}