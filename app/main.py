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
    if not host.isalnum():
        return 'Invalid input'
    sanitized_host = subprocess.quote(host)
    return safe_ping(sanitized_host)