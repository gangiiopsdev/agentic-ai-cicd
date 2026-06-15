from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return run_ping(host)