from fastapi import FastAPI
import subprocess
gl
app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    subprocess.run(args)
    return {"status": "completed"}