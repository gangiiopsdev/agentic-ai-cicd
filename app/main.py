from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host):
        # Replace shell=True with a list of arguments to avoid shell interpretation
        args = ['ping', '-c', '4', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = PingService.safe_ping(host)
    return {"status": "completed", "data": status}