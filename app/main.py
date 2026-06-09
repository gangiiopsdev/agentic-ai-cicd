from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and escape input to prevent shell injection
    host = shlex.quote(host)
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}