from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: str):
    args = shlex.split(command)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f'ping {host}'
    safe_subprocess(command)
    return {"status": "completed"}