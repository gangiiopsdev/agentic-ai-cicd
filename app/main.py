from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}