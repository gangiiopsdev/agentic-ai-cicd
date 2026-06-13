from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid code injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return "Invalid hostname"
    return safe_ping(host)