from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    safe_host_parts = [shlex.quote(part) for part in host.split()]
    return ' '.join(safe_host_parts)

@app.get('/ping')
def ping(host: str):
    safe_host = escape_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + safe_host.split(), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}