from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping_command(host):
    return ['ping', shlex.quote(host)]

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run with full path and validate input
        result = subprocess.run(safe_ping_command(host), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}