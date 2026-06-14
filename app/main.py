from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class App:
    def __init__(self):
        self.ping_service = PingService()

app = App()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return app.ping_service.ping(host)