from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}