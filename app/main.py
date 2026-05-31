from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum() or '@' in host or ':' in host or '/' in host:
            raise ValueError("Invalid host input")
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}