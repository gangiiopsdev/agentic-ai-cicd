from fastapi import FastAPI
import shlex
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping'] + [arg.strip() for arg in shlex.split(host) if arg.strip()]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)