from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    try:
        cmd = ['ping', '-c', '4'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)