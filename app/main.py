from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Fixed implementation using subprocess.run and list arguments
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)