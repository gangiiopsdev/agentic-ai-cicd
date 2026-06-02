from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', '-c', '4'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    if result.returncode != 0:
        raise Exception(result.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_ping(shlex.quote(host))
    return {"status": "completed", "output": result.stdout}