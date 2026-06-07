from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding shell=True
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError("Invalid hostname")
        ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 400