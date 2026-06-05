from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def safe_ping(self, host):
        if not host or host not in self.allowed_hosts:
            raise ValueError("Host cannot be empty or is not allowed")
        command = ['ping', '--{}'.format(host)]
        subprocess.run(command, check=True, text=True, capture_output=True)

app = FastAPI()
ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        return {
            "status": "completed",
            "output": ping_instance.safe_ping(host).stdout.strip() if host else ""
        }
    except ValueError as e:
        return {"error": str(e), "status": "failed"}