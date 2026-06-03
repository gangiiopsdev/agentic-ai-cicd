from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}