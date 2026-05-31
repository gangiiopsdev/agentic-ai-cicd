from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.call(['ping', f'"{host}"'])  # Use formatted string instead of shlex.quote for simplicity
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)