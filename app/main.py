from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str, *args):
    cmd_parts = [command] + list(args)
    full_cmd = shlex.join(cmd_parts)
    try:
        result = subprocess.run(full_cmd, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {e.stderr}"

def ping(host: str):
    return execute_command("ping", host)