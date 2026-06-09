from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}