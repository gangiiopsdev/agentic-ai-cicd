from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

async def ping(host: str):
    # Use os.path.abspath to ensure the executable path is full
    result = subprocess.run([os.path.abspath('ping'), '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)