from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        kwargs['shell'] = False
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        PingCommand(f"ping {host}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}