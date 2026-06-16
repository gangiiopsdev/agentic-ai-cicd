from fastapi import FastAPI
import subprocess
global_host = 'example.com' # Set this as a default or remove it if not needed

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str=global_host):
    # Fixed implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}