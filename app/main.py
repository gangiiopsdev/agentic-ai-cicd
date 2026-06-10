from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def is_safe(self):
        safe_hosts = ['google.com', 'example.com']
        return self.host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if PingCommand(host).is_safe():
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        raise ValueError('Unsafe hostname')