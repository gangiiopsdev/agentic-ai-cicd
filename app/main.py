from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper validation of input
    if not host.isdigit():
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': run_ping(host)}