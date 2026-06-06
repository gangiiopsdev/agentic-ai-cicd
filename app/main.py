from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1']

    def ping(self, host: str):
        if host in self.allowed_hosts and self.is_valid_host(host):
            subprocess.call(['ping', host])
        else:
            raise ValueError('Host not allowed')

    def is_valid_host(self, host: str):
        # Add more robust validation logic here
        return host.replace('.', '').isnumeric()

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):     
    safe_ping.ping(host)
    return {"status": "completed"}