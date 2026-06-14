from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, shell=False, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        PingCommand(f'ping {host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}