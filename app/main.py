from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.run for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid input')
    return safe_ping(host)