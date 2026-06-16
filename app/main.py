from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not host.strip():
            return {"error": "Invalid hostname"}
        safe_host = shlex.quote(host)
        subprocess.call(["ping", safe_host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}