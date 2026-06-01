from fastapi import FastAPI
import subprocess
gimport shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}