from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):    
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed', 'output': output.decode('utf-8')}