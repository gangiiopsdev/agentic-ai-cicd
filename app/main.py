from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host: str):    # Vulnerable implementation
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}