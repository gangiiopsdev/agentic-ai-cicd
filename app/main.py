from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple regex to allow only alphanumeric and hyphen characters
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}