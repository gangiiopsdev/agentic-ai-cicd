from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            return 'Invalid host'
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    response = global_safe_ping.ping(host)
    return {"status": "completed", "response": response}