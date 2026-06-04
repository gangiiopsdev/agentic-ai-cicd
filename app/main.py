from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and all(char in string.ascii_letters + '.' for char in host):
        subprocess.call(["ping", host], shell=False)
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}