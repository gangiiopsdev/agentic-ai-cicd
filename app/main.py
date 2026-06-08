from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    if not host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False, '', ''
    args = ['ping', '-c', '4', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return True, result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):     
    if not host or ' ' in host:
        return {'error': 'Invalid input'}
    status, output = safe_ping(host)    
    if status:
        return {'status': 'completed', 'output': output}
    else:
        return {'error': 'Invalid input'}