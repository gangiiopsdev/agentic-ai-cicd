from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use full path for 'ping' to avoid potential issues on different systems
        result = subprocess.run([os.path.join('/bin', 'ping'), host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}