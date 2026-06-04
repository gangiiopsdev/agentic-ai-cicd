from fastapi import FastAPI
import subprocess

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_fixed(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', subprocess.list2cmdline([host])]
        subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}