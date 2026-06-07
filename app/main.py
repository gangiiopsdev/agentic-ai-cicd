from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)