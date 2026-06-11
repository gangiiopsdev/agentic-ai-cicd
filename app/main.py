from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host against known safe values instead of only checking alphanumeric characters.
    if host not in ['google.com', 'example.com']:  # Replace with actual validation logic
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)