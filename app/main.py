from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', '127.0.0.1']  # Define allowed hosts here

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.call(['ping', host])
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)