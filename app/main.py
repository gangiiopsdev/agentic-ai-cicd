from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}