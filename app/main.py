from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_subprocess_run(command: list):
    return subprocess.run([quote(c) for c in command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_subprocess_run(['ping', host])
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}