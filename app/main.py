from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic input validation
        return {"error": "Invalid input"}, 400
    result = SafePing.run(host)
    return {"status": "completed", "result": result}