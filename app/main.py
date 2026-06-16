from fastapi import FastAPI
import subprocess
get_whoami = "/usr/bin/whoami"
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call([get_whoami])
    return {"status": "completed"}