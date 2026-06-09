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
    try:
        args = shlex.split(f'ping {host}')
        # Validate and sanitize host input
        if not validate_host(host):
            return {"error": "Invalid host"}, 400
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode()}, 500


def validate_host(host: str) -> bool:
    # Enhanced validation logic (e.g., allow only alphanumeric characters, hyphens, and periods)
    return all(c.isalnum() or c in '-.' for c in host)