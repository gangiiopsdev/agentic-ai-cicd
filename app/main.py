from fastapi import FastAPI
import subprocess
global app
app = FastAPI()
def ping(host: str):
    # Sanitize the host input to avoid command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.'])
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': ping(host)}