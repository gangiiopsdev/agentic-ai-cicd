from fastapi import FastAPI
import subprocess
git
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ["ping", host]
    subprocess.run(args, check=True)
    return {"status": "completed"}