from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingResponse(BaseModel):
    status: str

cmd = ['ping', '-c', '1']
dynamic_args = [host for host in host.split() if host.isalnum()]
if dynamic_args:
    cmd.extend(dynamic_args)

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> PingResponse:
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
        return PingResponse(status="completed with output: " + output.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status="failed with error: " + str(e))

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}