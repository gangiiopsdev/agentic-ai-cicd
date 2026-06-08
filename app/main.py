from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    return {'status': 'completed', 'output': safe_ping(host)}