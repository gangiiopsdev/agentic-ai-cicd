from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def execute_ping(host):
    # Safe implementation using subprocess.run with shell=False
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)