from fastapi import FastAPI
import subprocess

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            return {"status": "failed", "message": "Unauthorized host"}

        args = ['ping', host]
        subprocess.run(args, check=True)
        return {"status": "completed"}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)