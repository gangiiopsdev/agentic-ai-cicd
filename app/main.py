from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.command = ['ping', self.host]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing()
    safe_ping_instance.host = host
    result = subprocess.check_output(safe_ping_instance.command, stderr=subprocess.STDOUT)
    return {"status": "completed", "result": result.decode('utf-8')}