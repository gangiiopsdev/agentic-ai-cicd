from fastapi import FastAPI
import subprocess
glances = ['ping', 'google.com']
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(glances)
    return {"status": "completed"}