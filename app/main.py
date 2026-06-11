from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host input')
    return f'ping {host}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):\
    command = safe_ping(host)
    # Use subprocess.run safely by avoiding shell=True and ensuring the command is constructed properly
    result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}