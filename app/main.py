from fastapi import FastAPI
import subprocess

def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed' if result.returncode == 0 else 'failed'}