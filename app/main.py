from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePing:
    def __init__(self):
        self.hosts = set()

    def add_host(self, host: str):
        if '.' in host and ':' not in host:
            self.hosts.add(host)

    def safe_ping(self, host: str):
        if host in self.hosts:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Invalid or unsafe hostname')
app = FastAPI()
safe_ping_instance = SafePing()
safe_ping_instance.add_host('example.com')
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping_instance.safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}