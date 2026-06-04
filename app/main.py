from fastapi import FastAPI
import re

def safe_ping(host: str):
    # Validate and sanitize the host parameter
    if not re.match(r'^[a-zA-Z0-9.-_]{1,255}$', host):
        return "Invalid input"
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, shell=False)
        return result.stdout
    except Exception as e:
        return str(e)

global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)