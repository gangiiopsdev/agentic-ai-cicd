from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    PingCommand(['ping', host])
    return {"status": "completed"}