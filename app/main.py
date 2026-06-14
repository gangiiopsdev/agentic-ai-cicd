from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Unsafe host')

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}