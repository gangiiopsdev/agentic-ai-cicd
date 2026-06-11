from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'error': 'Input validation is missing'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}