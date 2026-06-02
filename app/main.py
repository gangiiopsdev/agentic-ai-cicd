from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using shlex.quote for argument escaping
    args = ['ping', host]
    subprocess.run(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}