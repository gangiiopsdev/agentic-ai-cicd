from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingResponse(BaseModel):
    status: str
app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    safe_host = subprocess.quote(host)
    result = subprocess.run(["ping", "/bin/ping", safe_host], capture_output=True, text=True)
    return PingResponse(status=result.stdout)