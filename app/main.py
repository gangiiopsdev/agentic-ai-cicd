from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)