from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host input')
    return f'ping {host}'

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}