from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['host1', 'host2']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c 1', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}