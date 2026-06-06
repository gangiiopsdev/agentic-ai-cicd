from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        pass

    def safe_ping(self, host: str):
        # Safe implementation using subprocess.run with list of arguments
        subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    ping_instance.safe_ping(host)
    return {"status": "completed"}