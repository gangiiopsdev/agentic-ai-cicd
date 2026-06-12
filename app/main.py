from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {"error": "Invalid hostname"}, 400
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}