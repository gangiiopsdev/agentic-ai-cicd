from fastapi import FastAPI
import shlex
import subprocess
def safe_ping(host: str):
    if host.isalnum() and len(host) < 256:
        # Use shlex.quote to safely escape the input
        safe_host = shlex.quote(host)
        subprocess.run(['ping', '-c', '1', safe_host], check=True)
class PingRequest(BaseModel):
    host: str
def ping(request: PingRequest):
    try:
        safe_ping(request.host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.post("/ping")
def ping_endpoint(request: PingRequest):
    return ping(request)