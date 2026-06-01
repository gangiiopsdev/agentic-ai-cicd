from fastapi import FastAPI
import subprocess
def safe_host(host):
    try:
        return host.isdigit()
    except AttributeError:
        return False
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not safe_host(host) or '&&' in host or ';' in host or '|'.in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}