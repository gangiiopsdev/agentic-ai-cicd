from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        if 'ping' not in host:
            return None
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafePing.safe_ping(host)
    if result is None:
        return {"error": "Invalid host"}
    else:
        return {"status": "completed", "result": result}