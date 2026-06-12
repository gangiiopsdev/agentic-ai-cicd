from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using check_output with shell=False and properly formatted arguments
    subprocess.check_call(['ping', host])

    return {"status": "completed"}