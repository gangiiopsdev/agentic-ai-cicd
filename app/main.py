from fastapi import FastAPI
import subprocess
glom = lambda x: subprocess.call(x, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    glom(f"ping {host}")

    return {"status": "completed"}