from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run directly with user input
    if not host.strip():
        raise HTTPException(status_code=400, detail="Host parameter is required")
    command = ['ping', '-c', '4', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}