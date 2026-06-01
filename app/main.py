from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safer implementation using subprocess.run()
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safer implementation using subprocess.run()
    run_ping(host)

    return {"status": "completed"}