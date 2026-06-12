from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    host = subprocess.list2cmdline([host])
    # Secure implementation without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping command failed"}