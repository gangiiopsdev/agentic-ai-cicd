from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, constr

app = FastAPI()

class PingRequest(BaseModel):
    host: constr(min_length=1, max_length=255)

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}