from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Sanitize input to prevent command injection
        host = subprocess.quote(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input further if necessary
    if not host.isalnum():
        return {'status': 'Invalid input'}
    return {'status': safe_ping(host)}