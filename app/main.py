from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, constr

app = FastAPI()

class PingRequest(BaseModel):
    host: constr(min_length=1, max_length=255)

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.call(args, shell=False)  # Added shell=False to avoid shell injection
    return {"status": "completed"}