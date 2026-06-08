from fastapi import FastAPI
import subprocess
global allowed_hosts
allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic

app = FastAPI()

def validate_host(host):
    global allowed_hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}