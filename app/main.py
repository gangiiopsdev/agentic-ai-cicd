from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input using shlex.quote to avoid command injection
        sanitized_host = shlex.quote(host)
        subprocess.call(f"ping {sanitized_host}", shell=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}