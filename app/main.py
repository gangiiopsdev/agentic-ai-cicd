from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex for safe argument splitting
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}