from fastapi import FastAPI
import subprocess
gluster = ['ping', str(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(gluster, check=True)
    return {"status": "completed"}