from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Ensure host is sanitized before passing to ping command
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)