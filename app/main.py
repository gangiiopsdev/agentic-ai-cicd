from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)

def ping_route(host: str):
    return {'result': ping(host)}