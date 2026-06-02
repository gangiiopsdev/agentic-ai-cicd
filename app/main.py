from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shlex.quote to escape any special characters in host
    subprocess.call(['ping', shlex.quote(host)])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape any special characters in host
    subprocess.call(['ping', shlex.quote(host)])