from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and splitting the command
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}