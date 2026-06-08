from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid input"
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}