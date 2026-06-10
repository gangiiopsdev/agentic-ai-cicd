from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host):
        super().__init__(args=['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, errors = command.communicate()
    if errors:
        return {"status": "error", "errors": errors.decode()}
    else:
        return {"status": "completed", "output": output.decode()}