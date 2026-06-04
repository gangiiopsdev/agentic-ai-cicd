from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with argument parsing to prevent injection
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, text=True)

    return {"status": "completed"}