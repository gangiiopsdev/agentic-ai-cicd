from fastapi import FastAPI
import subprocess
global_process = None

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global global_process
    if global_process is not None and global_process.poll() is None:
        global_process.terminate()

    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {"error": "Invalid input"}, 400

    global_process = subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return {"status": "completed"}