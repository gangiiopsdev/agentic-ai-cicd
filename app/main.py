from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if host.isalnum() and not any(char in '!@#$%^&*()_+\-=\[\]{}|;:,.<>?`~' for char in host):
        args = ['ping', host]
        subprocess.run(args, check=True)  # Use subprocess.run for better security
        return {"status": "completed"}
    else:
        return {"error": "Invalid host name"}