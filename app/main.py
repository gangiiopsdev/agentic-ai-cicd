from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

def _safe_host(host: str) -> str:
    if '.' in host or not host.replace('.', '').isdigit() and not host.isalnum():
        raise ValueError('Invalid host provided')
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    safe_host = _safe_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{safe_host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}