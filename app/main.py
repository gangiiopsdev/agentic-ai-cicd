from fastapi import FastAPI
import subprocess
import shlex
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }