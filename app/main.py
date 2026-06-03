from fastapi import FastAPI
import subprocess
import shlex
cimport re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid input")
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}