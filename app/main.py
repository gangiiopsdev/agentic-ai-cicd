from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str):
        return {'status': 'failed', 'error': result}
    else:
        return {'status': 'completed'}