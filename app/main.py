from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Secure implementation
    args = ["ping", request.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}