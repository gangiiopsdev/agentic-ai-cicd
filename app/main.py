from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    args = shlex.split('ping ' + shlex.quote(host))
    subprocess.run(args, check=True)
    return {"status": "completed"}