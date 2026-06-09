from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts