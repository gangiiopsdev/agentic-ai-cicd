from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}