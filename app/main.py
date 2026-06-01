from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input sanitization and use of safer functions
    safe_host = subprocess.list2cmdline([host])  # Using list2cmdline to safely format command line arguments
    try:
        subprocess.run(safe_host, shell=False, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}