from fastapi import FastAPI
import shlex
import subprocess
class Ping:
    def __init__(self):
        pass

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run for better control and security
    result = subprocess.run(shlex.split(f"ping {host}"), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}