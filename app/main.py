from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.hosts = set()

    def add_host(self, host: str):
        if '.' in host and ':' not in host:
            self.hosts.add(host)

    def safe_ping(self, host: str):
        if host in self.hosts:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "error", "output": "Host not allowed"}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping_instance.add_host(host)
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}