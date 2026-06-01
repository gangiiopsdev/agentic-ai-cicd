from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        return subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        SafeCommand.safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}