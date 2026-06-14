from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}