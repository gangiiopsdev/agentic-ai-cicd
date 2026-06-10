from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()
ping_instance = SafePing()

@app.get("/ping")
def ping_route(host: str):
    return ping_instance.ping(host)