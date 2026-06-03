from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex and validation
    if not host.strip():
        return {"status": "error", "output": "Invalid input"}
    args = shlex.split(f"ping {host}")
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}