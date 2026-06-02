from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or '.' not in host:
        return {'status': 'Invalid input'}
    return {'status': safe_ping(host)}