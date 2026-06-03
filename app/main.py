from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)