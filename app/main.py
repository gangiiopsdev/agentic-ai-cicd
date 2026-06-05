from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Use a full path for the executable to avoid partial path execution issues
    return subprocess.run(["/bin/ping", quote(host)], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "output": result.stderr}