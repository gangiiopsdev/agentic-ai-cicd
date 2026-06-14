from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def sanitize_host(host):
    safe_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return shlex.quote(safe_host)

@app.get('/ping')
def ping(host: str):
    # Sanitize host input
    safe_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}