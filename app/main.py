from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to ensure it only contains allowed characters
        if not host.isalnum():
            raise ValueError("Invalid host input")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return PingResponse(status=result.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status=e.stderr)