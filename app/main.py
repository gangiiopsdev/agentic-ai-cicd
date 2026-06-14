from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Secure implementation
    safe_host = subprocess.quote(host)
    result = subprocess.run(["ping", "-c", "1", safe_host], capture_output=True, text=True)
    return PingResponse(status=result.stdout)