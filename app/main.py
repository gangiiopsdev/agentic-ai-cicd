from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        return subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.safe_ping(host)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e), "status": "failed"}