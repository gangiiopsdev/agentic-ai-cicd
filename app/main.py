from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get('/ping')
def ping(request: PingRequest):
    command = ['ping', '-c', '1', request.host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}