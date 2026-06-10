from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = set(allowed_hosts)

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError("Host is not allowed")
        try:
            output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}

app = FastAPI()
safe_pinger = SafePinger(allowed_hosts=["google.com", "yahoo.com"])

@app.get("/ping")
def ping(host: str):
    return safe_pinger.ping(host)