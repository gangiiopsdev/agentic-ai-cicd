from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_hosts = {'google.com', 'example.com'}  # Define a set of allowed hosts

    def run(self, host: str):
        if host not in self.safe_hosts:
            return {'status': 'failed', 'message': 'Host is not allowed'}
        try:
            response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': response.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
safe_ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or ' ' in host:
        return {'status': 'invalid', 'message': 'Invalid input'}
    return safe_ping_service.run(host)