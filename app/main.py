from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shlex.quote to escape any special characters in the input
    subprocess.call(["ping", shlex.quote(host)])
    return {"status": "completed"}