from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using check_output instead of call
    output = subprocess.check_output(['ping', host], text=True)
    return {'status': 'completed', 'output': output}