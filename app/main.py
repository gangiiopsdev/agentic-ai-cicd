from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', 'localhost']

    def ping(self, host: str) -> bool:
        if host in self.allowed_hosts:
            command = ['ping', host]
            result = subprocess.run(command, capture_output=True, text=True)
            return True, result.stdout
        else:
            return False, 'Invalid host'

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, message = global_safe_ping.ping(host)
    if success:
        return {"status": "completed", "message": message}
    else:
        return {"status": "error", "message": message}