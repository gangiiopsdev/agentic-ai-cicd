from fastapi import FastAPI
import subprocess
def safe_ping(host):
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get('/ping/{host}')
def ping_endpoint(host: str):
    return safe_ping(host)