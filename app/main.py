from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host input")
    return safe_ping(host)
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host contains only allowed characters and formats.
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True