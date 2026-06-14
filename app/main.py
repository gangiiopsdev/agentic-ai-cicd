from fastapi import FastAPI
import subprocess
import shlex
git
app = FastAPI()
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        safe_ping(host)
        return {"status": "completed", "output": subprocess.getoutput(f'ping {host}').strip()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}