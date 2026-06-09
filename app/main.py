from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape special characters
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}