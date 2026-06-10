from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate input to prevent command injection
    if not host or not host.isalnum():
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')</code>