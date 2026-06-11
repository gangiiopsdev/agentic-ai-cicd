from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str, *args):
    cmd_parts = [command] + list(args)
    try:
        result = subprocess.run(cmd_parts, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {e.stderr}"
def ping(host: str):
    return execute_command("ping", host)