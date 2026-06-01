from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Basic validation of host
    if not host.isalnum():
        return 'Invalid host'
    # Sanitize and validate the host input further
    if not all(c.isalnum() or c in '.-:' for c in host):
        return 'Invalid host'
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}