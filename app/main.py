from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run with list of arguments instead of shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    return safe_ping(host)