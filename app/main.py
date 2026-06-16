from fastapi import FastAPI
import subprocess
def run_subprocess(command):
    return subprocess.run(command, check=True)