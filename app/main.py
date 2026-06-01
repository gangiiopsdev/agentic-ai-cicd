from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']  # Replace with actual allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 403
    subprocess.run(['ping', f'--host={host}'], check=True)
    return {"status": "completed"}