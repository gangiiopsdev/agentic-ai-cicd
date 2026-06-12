from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError("Invalid host name")
        subprocess.run(['ping', host], shell=False)

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        ping_service.safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400