from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def execute_safe_command(command, args):
    process = subprocess.Popen([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(request: PingRequest):
    command = 'ping'
    args = [request.host]
    output, error = execute_safe_command(command, args)
    if error:
        return {"status": "error", "message": str(error)}
    return {"status": "completed", "output": str(output)}