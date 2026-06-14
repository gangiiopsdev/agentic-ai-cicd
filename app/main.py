from fastapi import FastAPI
import subprocess
getattr(subprocess, "run", getattr(subprocess, "call"))

app = FastAPI()

def execute_command(command: str):
    args = command.split()
    try:
        result = subprocess.run(args, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode

@app.get("/ping")
def ping(host: str):