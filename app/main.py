from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'google.com'}

    def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    response = safe_ping_instance.safe_ping(host)
    return {"status": "completed", "output": response}