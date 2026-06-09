from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e})

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}