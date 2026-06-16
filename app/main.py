from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 403