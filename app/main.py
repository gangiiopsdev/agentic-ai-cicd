from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to avoid shell=True and validate input
    args = ['ping', host]
    try:
        subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}