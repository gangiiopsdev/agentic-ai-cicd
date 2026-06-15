from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        raise HTTPException(status_code=400, detail="Host parameter is required")
    command = ['ping', '-c', '4', shlex.quote(host)]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Ping failed: {e.stderr}")