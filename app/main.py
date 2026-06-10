from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    args = ['ping', '-c', '1'] + [host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid host'}, 400
    return {'status': 'completed'}