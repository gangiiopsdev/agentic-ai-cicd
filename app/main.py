from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list for arguments to avoid shell=True
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}