from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Ensure host input is sanitized or use a whitelist of allowed hosts
    if not host.strip().replace('.', '').isnumeric():
        return {"status": "failed", "error": "Invalid host format"}
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "result": result.stdout}