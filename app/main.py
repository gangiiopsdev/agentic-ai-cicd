from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    return safe_ping(host)