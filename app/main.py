from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def execute_ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = PingService.execute_ping(host)
    return {"status": "completed", "output": output}