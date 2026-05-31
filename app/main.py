from fastapi import FastAPI
import subprocess
def run_git_command(command):
    return subprocess.run(command, shell=False, capture_output=True, text=True)
git