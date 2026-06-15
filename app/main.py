from fastapi import FastAPI
import subprocess
import shlex
git
app = FastAPI()
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout.decode().strip()
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}