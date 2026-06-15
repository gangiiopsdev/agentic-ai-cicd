from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement hostname validation logic here
    allowed_hosts = ['example.com', 'test.example.com']
    return hostname in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}