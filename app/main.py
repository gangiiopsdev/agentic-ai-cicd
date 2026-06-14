from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely escape the host parameter
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}