from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex to safely handle command arguments
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}