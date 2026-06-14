from fastapi import FastAPI
import subprocess
import shlex

global allowed_hosts = ['127.0.0.1', '::1']

app = FastAPI()

async def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)