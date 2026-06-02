from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command: list):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    if shlex.split(host) != [host]:
        return {"status": "failed", "message": "Invalid input detected"}
    return safe_subprocess_call(command)