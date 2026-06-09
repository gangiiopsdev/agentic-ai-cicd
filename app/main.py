from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it only contains allowed characters
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host")

    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}