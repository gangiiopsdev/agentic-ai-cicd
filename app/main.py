from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping']

    def ping_host(self, host: str):
        try:
            return subprocess.run(self.ping_command + [subprocess.quote(host)], capture_output=True, text=True)
        except Exception as e:
            return str(e)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping_host(host: str):
    return ping_service.ping_host(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}