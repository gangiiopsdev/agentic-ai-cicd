from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Secure implementation with proper sanitization
    if host.isalnum() and '.' in host:
        cmd = ['ping', host]
        subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}