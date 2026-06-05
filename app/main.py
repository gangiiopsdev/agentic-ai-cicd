from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = "ping"
    args = shlex.split(host)
    result = subprocess.run([command] + args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}