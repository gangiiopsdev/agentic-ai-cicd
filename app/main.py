from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or '..' in host:
        raise HTTPException(status_code=400, detail="Invalid hostname")
    args = ['ping', '-c 1', host]  # Use '-c 1' to limit the number of pings
    subprocess.run(args, check=True)  # Use run instead of call for better error handling
    return {"status": "completed"}