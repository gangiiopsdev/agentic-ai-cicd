from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        # Validate host input
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError('Invalid host name')
        # Use subprocess.run with shell=False and safe arguments
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return run_ping(host)