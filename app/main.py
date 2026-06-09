from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.hosts = set()

    def ping(self, host: str):
        if host not in self.hosts:
            self.hosts.add(host)
            try:
                result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(e.stderr)

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)