from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Secure implementation\n    args = ['ping', request.host]\n    subprocess.run(args, check=True)\n    return {"status": "completed"}