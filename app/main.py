from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    safe_host = escape_host(host)
    subprocess.call(['ping', '-c', '1', safe_host], shell=False)
    return {'status': 'completed'}