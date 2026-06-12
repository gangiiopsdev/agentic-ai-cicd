from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex.quote to escape host input
    command = f"ping {shlex.quote(host)}"
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}