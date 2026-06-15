from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}

# Mount the app for testing purposes
app = global_app