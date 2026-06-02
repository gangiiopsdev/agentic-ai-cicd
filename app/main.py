from fastapi import FastAPI
import subprocess
def run_git_command(command):
    return subprocess.run(['git'] + command.split(), capture_output=True, text=True)
git