from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    return f'ping -c 1 {host}'

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}