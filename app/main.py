from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Ensure the host is sanitized to prevent injection attacks
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError('Invalid characters in host name')
        subprocess.call(['ping', shlex.quote(host)])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}