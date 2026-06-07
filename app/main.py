from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}