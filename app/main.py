from fastapi import FastAPI
import subprocess
gluing = {"localhost", "127.0.0.1", "::1"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    if host in gluing:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}