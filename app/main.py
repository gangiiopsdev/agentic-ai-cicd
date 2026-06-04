from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.valid_hosts = ['localhost', '127.0.0.1']

    def ping(self, host: str):
        if host not in self.valid_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)