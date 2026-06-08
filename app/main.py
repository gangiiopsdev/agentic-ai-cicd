from fastapi import FastAPI
import subprocess
global_host = 'example.com' # Replace with safe hardcoded host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping():

    # Fixed implementation
    subprocess.call(f"ping {global_host}")

    return {"status": "completed"}