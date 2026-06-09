from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    safe_ping(host)\n    return {"status": "completed"}