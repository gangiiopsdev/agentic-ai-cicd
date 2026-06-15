from fastapi import FastAPI
import subprocess
import shlex

class PingRequest:
    def __init__(self, host: str):
        self.host = shlex.split(host)

app = FastAPI()

@app.get('/ping')
def ping(ping_request: PingRequest):
    try:
        subprocess.run(['ping'] + ping_request.host, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}