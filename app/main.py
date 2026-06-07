from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(shlex.quote(host))  # Add shlex.quote to sanitize input
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500