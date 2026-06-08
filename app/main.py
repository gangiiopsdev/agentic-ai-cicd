from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command):
    return [arg.replace(';', ' ') for arg in command]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_command(["ping", host]))
    return {"status": "completed"}