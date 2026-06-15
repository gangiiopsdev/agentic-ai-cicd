from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(host: str = Depends(PingRequest)):
    # Use check_output for better security and capture the output
    result = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
    return {"status": "completed", "output": result}