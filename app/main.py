from fastapi import FastAPI
import subprocess
import shlex
class PingHost:
    def __init__(self):
        self.hosts = ['example.com']  # Replace with a list of trusted hosts

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if host not in PingHost().hosts:
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}