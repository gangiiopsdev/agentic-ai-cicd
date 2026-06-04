from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', '127.0.0.1']

    def is_safe_host(self, host: str) -> bool:
        return host in self.allowed_hosts

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if not safe_ping_instance.is_safe_host(host):
        raise ValueError('Invalid input for ping')
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)