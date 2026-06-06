from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}