from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str):
    if not host.strip() or '@' in host:
        raise ValueError('Invalid host parameter')
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        cmd = ['ping', sanitized_host]
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}