from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

@app.get('/ping', response_model=Dict[str, str])
def ping(host: str) -> Dict[str, str]:
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}