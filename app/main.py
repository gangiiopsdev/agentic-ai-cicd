from fastapi import FastAPI
import subprocess
from typing import Dict

def safe_ping(host: str) -> Dict[str, str]:
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str) -> Dict[str, str]:
    return safe_ping(host)