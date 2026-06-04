from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    def safe_ping(self, host):
        if not host or host not in self.allowed_hosts:
            raise ValueError("Host cannot be empty or is not allowed")
        subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()
ping_instance = SafePing()

@app.get="/ping")
def ping(host: str):
    try:
        result = ping_instance.safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}