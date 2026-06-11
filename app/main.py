from fastapi import FastAPI
import subprocess
import shlex

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Fixed implementation using subprocess.run with shell=False and explicit arguments
    command = shlex.split('ping ' + request.host)
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}