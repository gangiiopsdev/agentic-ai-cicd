from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.hosts = {'example.com': True, 'localhost': True}  # Allowlist of safe hosts

    def ping(self, host: str):
        if host not in self.hosts:
            return {'status': 'failed', 'error': 'Unauthorized host'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)