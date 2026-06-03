from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    if not os.path.exists(command[0]):
        raise ValueError(f"Command {command[0]} does not exist")
    subprocess.run(command, check=True)
    return {"status": "completed"}