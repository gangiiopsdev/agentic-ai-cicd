from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str): 
    try:
        if is_valid_host(host):
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}