from fastapi import FastAPI
import subprocess
from shlex import quote

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(["ping", quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}