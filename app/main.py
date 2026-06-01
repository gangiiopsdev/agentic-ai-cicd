from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

def ping(host: str):
    args = ['ping', '--count=1', quote(host)]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', '--count=1', quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}