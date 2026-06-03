from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self):
        self.allowed_hosts = ['example.com']  # Define allowed hosts

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.call(['ping', host])
        else:
            raise ValueError('Host not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    handler = PingHandler()\n    return handler.ping(host)