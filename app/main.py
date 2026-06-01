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
    # Ensure the host parameter is sanitized before use
    safe_host = host.strip()
    if len(safe_host) > 0 and '.' in safe_host.split()[0]:
        return safe_ping(safe_host)
    else:
        return "Invalid host provided"