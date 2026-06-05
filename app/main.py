from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        # Sanitize input to prevent command injection
        safe_host = ''.join(e for e in self.host if e.isalnum() or e.isdigit() or e == '.' or e == '-')
        subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    safe_ping.ping()
    return {"status": "completed"}