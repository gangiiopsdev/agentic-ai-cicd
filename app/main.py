from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        command = ['ping', '-c 1'] + shlex.split(request.host)
        subprocess.run(command, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}