from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        pass

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.split to avoid shell injection
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}