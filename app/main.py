from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    command = PingCommand(host=request.host)
    output = command.execute()
    return {"status": "completed", "output": output}