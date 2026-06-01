from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f"ping {host}"
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}