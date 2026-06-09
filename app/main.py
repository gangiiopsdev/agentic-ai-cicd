from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(host: str):
    ping_request = PingRequest(host)
    try:
        output = subprocess.run(['ping', '-c', '1', ping_request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}