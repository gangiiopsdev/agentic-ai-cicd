from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ["ping", host]
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}