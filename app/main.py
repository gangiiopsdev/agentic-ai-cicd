from fastapi import FastAPI
import subprocess
given_host = '8.8.8.8'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}