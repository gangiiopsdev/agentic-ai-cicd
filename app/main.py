from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])