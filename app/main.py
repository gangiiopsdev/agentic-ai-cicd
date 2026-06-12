from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host], shell=False)