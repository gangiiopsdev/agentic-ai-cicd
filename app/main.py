from fastapi import FastAPI
import subprocess

def generate_ping_command(host: str):
    return ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed", "result": result}