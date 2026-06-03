from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Host is not allowed to be pinged')
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.output}

app = FastAPI()
safe_ping = SafePing(allowed_hosts=['example.com'])

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)