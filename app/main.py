from fastapi import FastAPI
import subprocess
g-import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize and quote input to prevent shell injection
    safe_host = shlex.quote(host.strip())
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {"status": "completed"}