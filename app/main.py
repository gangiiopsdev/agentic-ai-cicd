from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input more thoroughly and use shlex to safely handle arguments
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}