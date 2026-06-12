from fastapi import FastAPI
import subprocess
import shlex

class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.post("/ping")
def ping_route(ping_request: PingRequest):
    try:
        result = subprocess.run(shlex.split(f'ping {ping_request.host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}