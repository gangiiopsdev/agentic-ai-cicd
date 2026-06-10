from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input before using it in subprocess
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}