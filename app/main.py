from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and passing arguments separately
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}