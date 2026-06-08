from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')
        args = ['ping', host]
        subprocess.call(args)

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        global_safe_ping.safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}