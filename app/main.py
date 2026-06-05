from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with check=True and capture_output=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)