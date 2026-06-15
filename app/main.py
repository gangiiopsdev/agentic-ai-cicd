from fastapi import FastAPI
import shlex
getattr(subprocess, "run", getattr(subprocess, "call"))

app = FastAPI()

def execute_command(command: str):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode

def ping(host: str):
    command = f"ping {host}"
    return execute_command(command)