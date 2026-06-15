from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return 'Invalid host'
    return run_ping(host)

def is_valid_host(host):\n    # Implement validation logic here, e.g., regex or allowed hosts list\n    return True