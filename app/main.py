from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() for c in host) or host == 'localhost'

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid_host'}
    subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, shell=False)
    return {'status': 'completed'}