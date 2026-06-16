from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is safe and escape command-line arguments
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', subprocess.list2cmdline([host])]
    subprocess.run(args, check=True)
    return {"status": "completed"}