from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}