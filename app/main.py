from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid host name"}
    ping_command = Ping().ping_command + [host]
    subprocess.run(ping_command, check=True)
    return {"status": "completed"}