from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    def ping(self, host: str):
        # Validate the input to prevent command injection
        safe_host = ''.join(filter(str.isalnum, host))  # Allow only alphanumeric characters
        subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {"status": "completed"}