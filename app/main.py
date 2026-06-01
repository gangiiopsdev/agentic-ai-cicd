from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape host
    from shlex import quote
    subprocess.call(f'ping {quote(host)}', shell=False)
    return {"status": "completed"}