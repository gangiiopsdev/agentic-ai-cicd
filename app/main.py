from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host.strip()
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    args = ['ping', '8.8.8.8']  # Replace with a known safe IP or use a whitelist
    subprocess.run(args, check=True)
    return {"status": "completed"}