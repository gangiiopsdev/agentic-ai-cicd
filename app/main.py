from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and argument list
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, capture_output=True)