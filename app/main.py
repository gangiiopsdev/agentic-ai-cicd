from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)