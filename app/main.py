from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def is_valid_host(host: str) -> bool:
    # Implement logic to validate the host input
    return True
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return safe_ping(host)