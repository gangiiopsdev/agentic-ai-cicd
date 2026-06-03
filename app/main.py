from fastapi import FastAPI
import subprocess
class PingCommandValidator:
    def __init__(self):
        self.allowed_hosts = {'google.com', 'example.com'}

    def validate_host(self, host: str) -> bool:
        return host in self.allowed_hosts

app = FastAPI()
ping_validator = PingCommandValidator()
def safe_ping(host: str):
    if ping_validator.validate_host(host):
        args = ['ping', host]
        subprocess.run(args)
    else:
        raise ValueError('Host not allowed')
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}