from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.strip():
        return 'Invalid host'
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}