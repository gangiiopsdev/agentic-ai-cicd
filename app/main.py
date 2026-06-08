from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host):
    try:
        # Use subprocess.run instead with shell=False and appropriate arguments
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return ping_host(host)