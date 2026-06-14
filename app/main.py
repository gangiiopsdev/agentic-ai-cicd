from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host: str):
        if not host.isalnum() or len(host) > 50:
            raise ValueError("Invalid hostname")
        self.host = host

    def run(self):
        result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        ping_host = PingHost(host)
        return ping_host.run()
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}