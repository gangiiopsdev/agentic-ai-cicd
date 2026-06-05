from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(['ping', host], check=True)