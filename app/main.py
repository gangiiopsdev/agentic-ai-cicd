from fastapi import FastAPI
import subprocess
def check_host(host):
    if not all(c.isalnum() or c in '._-' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get('/ping')
def ping_host_endpoint(host: str):
    return check_host(host)