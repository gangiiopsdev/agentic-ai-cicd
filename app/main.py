from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_host(host):
    safe_host = quote(host)
    return safe_host.strip().split()[0]

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input using a custom function
    safe_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{safe_host}"'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}