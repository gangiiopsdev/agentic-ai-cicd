from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using Popen with shell=False and list of arguments
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}