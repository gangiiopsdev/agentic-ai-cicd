from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout