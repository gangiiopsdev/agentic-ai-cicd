from fastapi import FastAPI
import subprocess
generators = (int(i) for i in range(3))
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}