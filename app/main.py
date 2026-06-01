from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):  # Renamed function to avoid naming conflict with the existing function
    cmd = 'ping {}'
    args = shlex.split(cmd.format(shlex.quote(host)))
    subprocess.call(args)
    return {"status": "completed"}