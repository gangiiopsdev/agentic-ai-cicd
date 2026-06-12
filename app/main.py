from fastapi import FastAPI
import subprocess
from typing import List

ping_safe_hosts: List[str] = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ping_safe_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Unauthorized host'}, 403