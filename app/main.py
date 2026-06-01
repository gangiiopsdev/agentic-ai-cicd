from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Sanitize user input using shlex.quote
        command = ['ping', '-c', '1', shlex.quote(request.host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}