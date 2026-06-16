from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
    return {
        "status": "completed",
        "output": output
    }