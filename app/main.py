from fastapi import FastAPI
import subprocess
generate_safe_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(generate_safe_command(host))
    return {"status": "completed"}