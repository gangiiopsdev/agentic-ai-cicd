from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        cmd = ['ping'] + shlex.split(host)
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}