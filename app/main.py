from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    # Use shell=False to prevent execution of untrusted input as a shell command
    subprocess.run(args, check=True, shell=False)

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}