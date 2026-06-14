from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
global app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping_route(host: str):
    response = PingService.ping(host)
    return {"status": "completed", "response": response}