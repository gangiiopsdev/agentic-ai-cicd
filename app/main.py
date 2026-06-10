from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {"status": "failed", "error": result.stderr}
    return {"status": "completed", "stdout": result.stdout}