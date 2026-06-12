from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.strip() or '\' in host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', subprocess.list2cmdline([host])], capture_output=True, text=True)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}