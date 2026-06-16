from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(shlex.quote(host))
    return {"status": "completed", "output": output}