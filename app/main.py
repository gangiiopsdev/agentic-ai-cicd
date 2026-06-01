from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use a safe command
    safe_host = host.strip()[:100]  # Limit length to prevent excessive input
    try:
        subprocess.run(["ping", safe_host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}