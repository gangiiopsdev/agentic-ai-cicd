from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        args = ['ping', '-c', '1', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str): 
    safe_ping = SafePing(host)
    safe_ping.ping()
    return {"status": "completed"}