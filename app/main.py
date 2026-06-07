from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = global_safe_ping(host)
    return {"status": "completed", "output": output}