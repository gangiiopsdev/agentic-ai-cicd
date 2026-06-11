from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not PingCommand().is_safe_host(host):\n        raise ValueError("Invalid host")\n    subprocess.call(f"ping {host}", shell=False)\n    return {"status": "completed"}