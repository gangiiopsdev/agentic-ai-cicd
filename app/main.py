from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
def validate_host(host: str) -> bool:
    # Basic validation of the host, not exhaustive
    return all(c.isalnum() or c in '.-' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    if validate_host(request.host):
        subprocess.call(f"ping {request.host}", shell=True)
    else:
        return{"status": "invalid host"}
    return {"status": "completed"}