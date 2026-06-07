from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = set(['127.0.0.1', 'localhost'])

    def ping(self, host: str):
        if host not in self.safe_hosts:
            return {'status': 'error', 'message': 'Invalid hostname'}
        # Validate and sanitize the input before passing to subprocess
        sanitized_host = shlex.quote(host)
        try:
            result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)