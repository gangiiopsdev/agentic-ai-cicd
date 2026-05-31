from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid host input")
        result = subprocess.run(shlex.split(f'ping -- {host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}