from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)