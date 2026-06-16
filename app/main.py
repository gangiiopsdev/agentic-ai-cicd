from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(e)

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}