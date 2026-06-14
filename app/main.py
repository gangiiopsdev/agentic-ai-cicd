from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input more thoroughly and use a whitelist
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host name")
    command = ["ping", host]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}