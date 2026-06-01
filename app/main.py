from fastapi import FastAPI
import subprocess
def run_git_command(command):
    try:
        result = subprocess.run(command.split(), shell=False, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
git