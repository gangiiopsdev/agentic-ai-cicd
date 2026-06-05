from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    try:
        return await safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}