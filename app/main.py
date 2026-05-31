from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Safe implementation
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    ping_service.ping(host)
    return {"status": "completed"}