from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using subprocess.run and validating input
    if not host or not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}