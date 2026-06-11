from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def safe_ping(host):
        try:
            return subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or ' ' in host:
        return {"status": "error", "result": "Invalid input"}
    result = SafePinger.safe_ping(host)
    return {"status": "completed", "result": result}