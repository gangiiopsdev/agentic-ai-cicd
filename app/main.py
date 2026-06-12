from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'error': 'Invalid host input'}, 400
    try:
        subprocess.call(['ping', sanitized_host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400