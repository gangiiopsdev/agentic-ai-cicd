from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

# Ensure that the host input is validated or sanitized if used in a production environment
global_safe_ping = SafePing('127.0.0.1')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(", '.join(filter(str.isalnum, host.split('.'))))
    result = safe_ping.execute()
    return {"status": "completed", "result": result}