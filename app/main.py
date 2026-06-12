from fastapi import FastAPI
import subprocess
class SanitizeInput:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def sanitize(self, host: str) -> str:
        if host in self.allowed_hosts:
            return host
        else:
            raise ValueError('Invalid host')

app = FastAPI()
sanitize_input = SanitizeInput()

def ping(host: str):
    try:
        host = sanitize_input.sanitize(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)