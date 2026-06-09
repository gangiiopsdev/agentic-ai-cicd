from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)