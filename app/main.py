from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host not in self.safe_hosts:
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping.ping(host)
    except ValueError as e:
        return {"status": "failed", "error": str(e)}