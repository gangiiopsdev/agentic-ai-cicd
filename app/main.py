from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str) -> bool:
    return all(c not in host for c in [';', '&', '|', '*', '?', '<', '>'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input detected"}
    args = ['ping', quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}