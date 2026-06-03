from fastapi import FastAPI
import subprocess
import shlex

def run_git_command(command):
    if not isinstance(command, str) or not command.strip().startswith('git '):
        raise ValueError("Invalid command")
    args = shlex.split(command)
    # Use shell=False and check the returncode explicitly
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    if result.returncode != 0:
        raise Exception(result.stderr.strip())
    return result.stdout