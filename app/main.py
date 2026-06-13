from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}