from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen instead of shell=True
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host does not contain harmful characters
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)