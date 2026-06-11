from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result.stdout}