from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}