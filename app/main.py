from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def ping(self, host: str):
        if host in self.allowed_hosts:
            try:
                output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
                return {"status": "completed", "output": output.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": str(e)}
        else:
            return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()
safe_ping = SafePing(['example.com', 'test.com'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)