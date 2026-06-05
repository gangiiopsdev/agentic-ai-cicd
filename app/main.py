from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid hostname'
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}