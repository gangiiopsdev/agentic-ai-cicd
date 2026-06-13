from fastapi import FastAPI
import subprocess
cimport = ["ping"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.run(cimport + [host], check=True)

    return {"status": "completed"}