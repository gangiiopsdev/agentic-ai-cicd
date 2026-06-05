from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "output": "Invalid host"}
    return safe_ping(host)