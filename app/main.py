from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        cmd = PingCommand(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = cmd.communicate()
        return {"status": "completed", "output": stdout.decode()}
    except Exception as e:
        return {"error": str(e)}