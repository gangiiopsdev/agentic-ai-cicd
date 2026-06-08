from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex.quote to safely escape the host argument
        safe_host = shlex.quote(host)
        subprocess.call(f"ping {safe_host}", shell=True)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}