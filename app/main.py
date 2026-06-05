from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = f'ping -c 1 {host}'  # Use f-string for safe string formatting
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False)
    return {"status": "completed", "output": result.stdout}