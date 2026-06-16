from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping_safe(host: str):
    # Validate host to ensure it only contains allowed characters (e.g., alphanumeric and some special characters)
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': ping_safe(host)}