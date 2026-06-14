from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

gt
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

gt
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}