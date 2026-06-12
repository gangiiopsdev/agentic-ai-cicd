from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError("Invalid hostname")
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c 1', '8.8.8.8'], check=True, shell=False)  # Replace with a trusted target

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError("Invalid hostname")
        safe_host = shlex.quote(host)
        subprocess.run(['ping', '-c 1', '8.8.8.8'], check=True, shell=False)  # Replace with a trusted target
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 400