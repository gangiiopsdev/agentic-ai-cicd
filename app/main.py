from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        args = ['ping', '-c', '1', host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.safe_ping(host)
        return {"status": "completed", "result": result.stdout}
    except Exception as e:
        return {"error": str(e), "status": "failed"}