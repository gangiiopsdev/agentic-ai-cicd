from fastapi import FastAPI
import subprocess
gitignored_ips = ['127.0.0.1', 'localhost']  # Add more IPs as needed

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in gitignored_ips:
        args = ['ping', host]
        subprocess.run(args, check=True)
    return {"status": "completed"}