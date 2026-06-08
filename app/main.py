from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        args = ['ping', '--'] + [host]  # Use -- to prevent options injection
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent unexpected behavior
        return {"status": "error", "result": "Invalid input"}
    result = SafePing.run(host)
    return {"status": "completed", "result": result}