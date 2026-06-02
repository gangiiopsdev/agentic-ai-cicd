from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    def ping(self, host: str):
        if host in self.allowed_hosts:
            try:
                result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
                return {"status": "completed", "output": result.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": str(e)}
        else:
            return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()
safe_pinger = SafePinger(allowed_hosts=['127.0.0.1', '::1'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_pinger.ping(host)