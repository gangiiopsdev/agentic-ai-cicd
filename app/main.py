from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host!r}')  # Use !r for safe string representation
    subprocess.run(args, check=True)
    return {"status": "completed"}