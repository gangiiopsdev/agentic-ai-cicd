from fastapi import FastAPI
import subprocess
global completed
completed = False
def ping(host: str):
    global completed
    # Safer implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode == 0:
        completed = True
    return {'status': 'completed' if completed else 'failed'}