from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Escape any shell metacharacters in the input
    escaped_host = shlex.quote(host)
    subprocess.run(['ping', escaped_host], check=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}