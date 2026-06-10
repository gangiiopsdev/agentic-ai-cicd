from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    return {'status': 'completed'}