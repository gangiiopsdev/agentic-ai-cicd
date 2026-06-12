from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent shell injection
    if not host.isalnum() or ';' in host:
        return {"status": "error", "message": "Invalid host"}
    escaped_host = subprocess.list2cmdline([host])
    result = subprocess.run(['ping', '-c', '1'] + [escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}