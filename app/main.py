from fastapi import FastAPI
import subprocess
given_host = host.strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', given_host])

    return {"status": "completed"}