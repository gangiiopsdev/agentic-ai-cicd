from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ("-", ".", "_") for c in host):
        return {"error": "Invalid hostname"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}