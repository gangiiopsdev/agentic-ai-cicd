from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def validate_host(self, host):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid hostname')

    def ping(self, host):
        self.validate_host(host)
        subprocess.run(['ping', '-c 4', host], check=True)

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):\n    return safe_ping.ping(host)