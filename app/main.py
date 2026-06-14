from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    args = ['ping', *shlex.split(host)]
    subprocess.run(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}