from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    @staticmethod
    def validate_host(host):
        allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
        return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if PingCommand.validate_host(host):
        subprocess.call(f"ping {host}", shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}