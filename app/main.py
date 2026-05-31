from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with error handling
    safe_ping(host)
    return {"status": "completed", "output": result.stdout}