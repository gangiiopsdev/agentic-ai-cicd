from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_cmd = ['ping', '{}']

    def safe_ping(self, host):
        # Using subprocess.run with shell=False and args parameter for a safer implementation
        subprocess.run(self.ping_cmd.format(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.safe_ping(host)
    return {"status": "completed"}