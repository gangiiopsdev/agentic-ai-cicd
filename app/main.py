from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Sanitize input
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return secure_ping(host)