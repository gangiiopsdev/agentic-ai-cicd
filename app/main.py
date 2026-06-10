from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/")
    def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}

    @app.get("/ping")
    def ping(self, host: str):
        if not host.isalnum() or '@' in host:
            raise ValueError('Invalid input for hostname')
        result = safe_ping(host)
        return {"status": "completed", "output": result}
safe_ping_instance = SafePing()