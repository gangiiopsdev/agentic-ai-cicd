from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(host)
    # Secure implementation
    try:
        subprocess.run(f"ping {escaped_host}", shell=False, check=True)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e)}