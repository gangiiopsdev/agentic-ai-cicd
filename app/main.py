from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input against shell metacharacters and ensure it's not empty
        if not all(c.isalnum() or c in ['.', '-', ''] for c in host) or len(host.strip()) == 0:
            raise ValueError("Invalid host name")
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}