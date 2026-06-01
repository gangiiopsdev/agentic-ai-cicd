from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_call(command):
        return subprocess.run(['ping', command], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_call(host)
    return {"status": "completed", "output": result.stdout}