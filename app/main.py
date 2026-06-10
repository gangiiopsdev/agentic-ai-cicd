from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or not isinstance(host, str) or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', '-c', '4', host]
    args = shlex.split(' '.join(command))
    try:
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)