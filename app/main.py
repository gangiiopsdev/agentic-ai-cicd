from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def safe_ping(self, host):
        if not host or host not in self.allowed_hosts:
            raise ValueError("Host cannot be empty or is not allowed")
        subprocess.call(['ping', host])

app = FastAPI()
ping_instance = SafePing()

@app.get="/ping")
def ping(host: str):
    try:
        return {"status": "completed", "output": ping_instance.safe_ping(host)}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}