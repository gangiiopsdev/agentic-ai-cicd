from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = shlex.quote(host)
    args = shlex.split(f"ping {safe_host}")
    result = subprocess.run(args, check=True, capture_output=True)
    return {
        "status": "completed",
        "output": result.stdout.decode()
    }