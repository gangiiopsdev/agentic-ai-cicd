from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation using subprocess.Popen
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)