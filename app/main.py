from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: str, *args):
    if isinstance(command, list):
        return subprocess.run(command, check=True)
    else:
        args = shlex.split(args[0])
        command_list = [command] + args
        return subprocess.run(command_list, check=True)

@app.get("/ping")
def ping(host: str):
    safe_subprocess('ping', host)
    return {"status": "completed"}