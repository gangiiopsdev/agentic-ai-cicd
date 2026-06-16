from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to allow only alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {"status": "error", "message": "Invalid hostname"}
    # Secure implementation
    try:
        result = subprocess.run(["ping", host], check=True, shell=False, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}