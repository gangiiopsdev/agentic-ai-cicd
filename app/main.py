from fastapi import FastAPI
import re
import subprocess

global app = FastAPI()

def validate_input(host):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and '.' in host:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if validate_input(host):
        args = ['ping', subprocess.escape(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        return {'error': 'Invalid input'}