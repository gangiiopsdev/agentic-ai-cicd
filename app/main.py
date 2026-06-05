from fastapi import FastAPI
import subprocess
import os
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use full path for 'ping' and sanitize input to avoid potential issues on different systems
        args = [os.path.join('/bin', 'ping'), shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}