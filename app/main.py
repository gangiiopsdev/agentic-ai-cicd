from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_hostname(hostname):
    return all(c.isalnum() or c in '-.' for c in hostname)

@app.get('/ping')
def ping(host: str):
    if not is_valid_hostname(host):
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}