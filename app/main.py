from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}