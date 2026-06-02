from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Sanitize user input by escaping special characters
    safe_host = shlex.quote(host)
    args = shlex.split(f"ping {safe_host}")
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}