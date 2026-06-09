from fastapi import FastAPI
import subprocess
import re
def is_valid_host(host):
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, host) is not None
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host address")
    subprocess.run(['ping', f'localhost']), check=True)
    return {"status": "completed"}