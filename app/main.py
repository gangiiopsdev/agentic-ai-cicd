from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ['ping', host]
    subprocess.run(command_parts, check=True, shell=False)
    return {"status": "completed"}