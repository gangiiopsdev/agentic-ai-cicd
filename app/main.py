from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = set(['127.0.0.1', 'localhost'])

    def ping(self, host: str):
        if host not in self.safe_hosts:
            return {"status": "error", "message": "Invalid hostname"}
        subprocess.run(shlex.split(f'ping {host}'), check=True)
        return {"status": "completed"}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)