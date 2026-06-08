from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using a list to pass arguments instead of shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate the input
        raise ValueError("Invalid host name")
    return ping(host)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}