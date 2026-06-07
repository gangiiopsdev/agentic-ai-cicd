from fastapi import FastAPI
import subprocess
import shlex
global app
global HOST
app = FastAPI()
HOST = "localhost"
@app.get("/ping")
def ping(host: str):
    if host == HOST:
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout, "error": result.stderr}
    return {"status": "completed"}